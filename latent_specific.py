import os
import time
import math
import argparse
import torch
import numpy as np

##### This is exactly how the original code generated its random samples

dimOfLatentCode = 256
device = 'cuda'
save_dir = './latentCode'

parser = argparse.ArgumentParser()
latentCode_np = np.vstack((np.repeat(np.float32(-2), dimOfLatentCode),
                           np.repeat(np.float32(-1), dimOfLatentCode),
                           np.repeat(np.float32(0), dimOfLatentCode),
                           np.repeat(np.float32(1), dimOfLatentCode),
                           np.repeat(np.float32(2), dimOfLatentCode),))
np.save(os.path.join(save_dir, 'latentCode.npy'), latentCode_np)