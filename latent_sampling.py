from scipy.interpolate import interp1d
import numpy as np

numOfSamples = 10

#### Line sampling
endpoint1 = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3])
endpoint2 = np.array([5, 4, 3, 2, 1, 0, 1, 3, 2])
interpolation = interp1d([0,numOfSamples-1], np.vstack([endpoint1, endpoint2]), axis=0)
steps = np.arange(0,numOfSamples)
samples = interpolation(steps)
print(samples.shape)
print(samples)