import os
import time
import math
import argparse
import torch
from tqdm.auto import tqdm

from utils.dataset import *
from utils.misc import *
from utils.data import *
from models.vae_gaussian import *
from models.vae_flow import *
from models.flow import add_spectral_norm, spectral_norm_power_iteration
from evaluation import *


import asyncio
import websockets
import json
import numpy as np

dimOfLatentCode = 256

categories = None
ckpt = None
dataset_path = None
log_dir = None
normalize = None
batch_size = None
device = None
sample_num_points = None

logger = None
model = None
test_dset = None

testLatentCode_path ="./testingWebApp/data/testLatentCode.npy"
testPointCloud_path = "./testResult/out.npy"


def normalize_point_clouds(pcs, mode, logger):
    if mode is None:
        logger.info('Will not normalize point clouds.')
        return pcs
    logger.info('Normalization mode: %s' % mode)
    for i in tqdm(range(pcs.size(0)), desc='Normalize'):
        pc = pcs[i]
        if mode == 'shape_unit':
            shift = pc.mean(dim=0).reshape(1, 3)
            scale = pc.flatten().std().reshape(1, 1)
        elif mode == 'shape_bbox':
            pc_max, _ = pc.max(dim=0, keepdim=True) # (1, 3)
            pc_min, _ = pc.min(dim=0, keepdim=True) # (1, 3)
            shift = ((pc_min + pc_max) / 2).view(1, 3)
            scale = (pc_max - pc_min).max().reshape(1, 1) / 2
        pc = (pc - shift) / scale
        pcs[i] = pc
    return pcs


async def handler(websocket):
    async for message in websocket:
        ###################################################### Parse Request
        request = json.loads(message)
        requestId = request["requestId"]
        #print(requestId)
        latentCodes = request["latentCodes"]
        #print(latentCodes)

        ####################################################### Generate
        gen_pcs = []
        with torch.no_grad():
            print("################")
            print(device)
            z = torch.from_numpy(np.asarray(latentCodes, dtype=np.float32)).to(device)
            assert z.shape[1] == dimOfLatentCode
            # z = torch.from_numpy(np.load(args.latentCode_path)).to(args.device)
            x = model.sample(z, sample_num_points, flexibility=ckpt['args'].flexibility)
            gen_pcs.append(x.detach().cpu())
        gen_pcs = torch.cat(gen_pcs, dim=0)[:len(test_dset)]
        if normalize is not None:
            gen_pcs = normalize_point_clouds(gen_pcs, mode=normalize, logger=logger)

        # Save generate pointclouds for debugging
        logger.info('Saving point clouds...')
        np.save(os.path.join(log_dir, 'out.npy'), gen_pcs.numpy())


        ####################################################### Respond
        testLatentCode = np.load(testLatentCode_path)
        testPointCloud = np.load(testPointCloud_path)
        examplePC = json.dumps({"requestId": "exampleID", 
                                "latentCodes": testLatentCode.tolist(), 
                                "pointClouds": testPointCloud.tolist()})
        await websocket.send(examplePC)


# entry point
async def main():
    global categories
    global ckpt
    global dataset_path
    global log_dir
    global normalize
    global batch_size
    global device
    global sample_num_points

    global logger
    global model
    global test_dset

    categories = ['chair']
    ckpt = './pretrained/GEN_chair.pt'
    dataset_path = './data/shapenet.hdf5'
    log_dir = "./serverLogs"
    normalize = 'shape_bbox'
    batch_size = 128
    device = 'cuda'
    sample_num_points = 2048

    ################################# Setup and Load Model
    # Logging
    # save_dir = os.path.join(args.log_dir, 'GEN_Ours_%s_%d' % ('_'.join(args.categories), int(time.time())) )
    # if not os.path.exists(save_dir):
    #     os.makedirs(save_dir)
    logger = get_logger('test', log_dir)
    # for k, v in vars(args).items():
    #     logger.info('[ARGS::%s] %s' % (k, repr(v)))

    # Checkpoint
    ckpt = torch.load(ckpt)
    # seed_all(args.seed)

    # Datasets and loaders
    logger.info('Loading datasets...')
    test_dset = ShapeNetCore(
        path=dataset_path,
        cates=categories,
        split='test',
        scale_mode=normalize,
    )
    test_loader = DataLoader(test_dset, batch_size=batch_size, num_workers=0)

    # Model
    logger.info('Loading model...')
    if ckpt['args'].model == 'gaussian':
        model = GaussianVAE(ckpt['args']).to(device)
    elif ckpt['args'].model == 'flow':
        model = FlowVAE(ckpt['args']).to(device)
    logger.info(repr(model))
    # if ckpt['args'].spectral_norm:
    #     add_spectral_norm(model, logger=logger)
    model.load_state_dict(ckpt['state_dict'])

    # Reference Point Clouds
    ref_pcs = []
    for i, data in enumerate(test_dset):
        ref_pcs.append(data['pointcloud'].unsqueeze(0))
    ref_pcs = torch.cat(ref_pcs, dim=0)

    ################################# Setup Websocket Handler 
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())


