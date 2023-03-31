from scipy.interpolate import interp1d
import numpy as np

#### Line sampling
numOfSamples_line = 10
ep1 = np.array([-2, -1, 0, 1, 2, 3])
ep2 = np.array([2, 1, 0, 1, 3, 2])
assert ep1.shape == ep2.shape
print(np.vstack([np.expand_dims(ep1,0), np.expand_dims(ep2,0)]).shape)

def lineSampling(endpoint1, endpoint2, numOfSamples, axis=0): 
    interpolation = interp1d([0,numOfSamples-1], np.vstack([np.expand_dims(endpoint1,0), np.expand_dims(endpoint2,0)]), axis=axis)
    steps = np.arange(0,numOfSamples)
    samples = interpolation(steps)
    return samples

s = lineSampling(ep1, ep2, numOfSamples_line)
assert s.shape == (numOfSamples_line, ep1.shape[0])
print(s.shape)
print(s)

### Grid sampling given four corners
numOfSamples_line2 = 5
corner1 = np.array([-2, -1, 0, 1, 2, 3])
corner2 = np.array([2, 1, 0, 1, 3, 2])
corner3 = np.array([30, 20, 10, 20, 40, 30])
corner4 = np.array([20, 10, 0, 10, 30, 20])

ls1 = lineSampling(corner1, corner2, numOfSamples_line)
ls2 = lineSampling(corner3, corner4, numOfSamples_line)
print(np.vstack([np.expand_dims(ls1,0), np.expand_dims(ls2,0)]).shape)

samples_grid = lineSampling(ls1, ls2, numOfSamples_line2)
print(samples_grid.shape)
print(samples_grid)
