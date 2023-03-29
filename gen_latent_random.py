import os
import time
import math
import argparse
import torch
import numpy as np

##### This is exactly how the original code generated its random samples

numOfCodeToGen = 1
dimOfLatentCode = 256
device = 'cuda'
save_dir = './latentCode'

parser = argparse.ArgumentParser()
latentCode = torch.randn([numOfCodeToGen, dimOfLatentCode])
np.save(os.path.join(save_dir, 'latentCode.npy'), latentCode.numpy())