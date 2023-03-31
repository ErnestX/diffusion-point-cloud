from scipy.interpolate import interp1d
import numpy as np

numOfSamples = 10

#### Line sampling
endpoint1 = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4])
endpoint2 = np.array([5, 4, 3, 2, 1, 0, 1, 3, 2, 1])
interpolation = interp1d([0,numOfSamples-1], np.vstack([endpoint1, endpoint2]), axis=0)
steps = np.arrange(0,numOfSamples)
samples = interpolation(steps)
print(samples.shape)
print(samples)