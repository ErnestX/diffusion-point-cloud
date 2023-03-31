from scipy.interpolate import interp1d
import numpy as np

#### Line sampling
def lineSampling(endpoint1, endpoint2, numOfSamples, axis=0): 
    interpolation = interp1d([0,numOfSamples-1], np.vstack([np.expand_dims(endpoint1,0), np.expand_dims(endpoint2,0)]), axis=axis)
    steps = np.arange(0,numOfSamples)
    samples = interpolation(steps)
    return samples

numOfSamples_line = 10
ep1 = np.array([-2, -1, 0, 1, 2, 3])
ep2 = np.array([2, 1, 0, 1, 3, 2])
assert ep1.shape == ep2.shape
print(np.vstack([np.expand_dims(ep1,0), np.expand_dims(ep2,0)]).shape)

s = lineSampling(ep1, ep2, numOfSamples_line)
assert s.shape == (numOfSamples_line, ep1.shape[0])
print(s.shape)
print(s)



### Grid sampling given four corners
def gridSampling(corner1, corner2, cornerA, cornerB, numOfSamples1, numOfSamples2):
    dim = corner1.shape[0]
    samples_line1 = lineSampling(corner1, corner2, numOfSamples1)
    samples_line2 = lineSampling(cornerA, cornerB, numOfSamples1)
    samples_grid = lineSampling(samples_line1, samples_line2, numOfSamples_line2)    
    return samples_grid

numOfSamples_line2 = 5
c1 = np.array([-2, -1, 0, 1, 2, 3])
c2 = np.array([2, 1, 0, 1, 3, 2])
cA = np.array([30, 20, 10, 20, 40, 30])
cB = np.array([20, 10, 0, 10, 30, 20])
assert c1.shape == c2.shape == cA.shape == cB.shape

s_grid = gridSampling(c1, c2, cA, cB, numOfSamples_line, numOfSamples_line2)
print(s_grid.shape)
assert s_grid.shape == (numOfSamples_line2, numOfSamples_line, c1.shape[0])
print(s_grid)


### Distance between points
def distanceBetweenPoints(point1, point2):
    return np.linalg.norm(point1-point2)

p1 = np.array([0,0])
p2 = np.array([3,4])
assert distanceBetweenPoints(p1, p2) == 5

p3 = np.array([-2, -1, 0, 1, 2, 3])
p4 = np.array([0, -1, 0, 1, 2, 3])
assert distanceBetweenPoints(p3, p4) == 2
