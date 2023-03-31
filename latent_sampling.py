from scipy.interpolate import interp1d
import numpy as np
import math

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


### Translate to MiniMap Visualization Coordinates
scale = 1

origin = np.array([-2, -1, 0, 1, 2, 3]) # the origin goes at (0,0,0) 
coord_origin = np.array([0, 0, 0])

anchor1 = np.array([-20, -10, 0, -10, -30, 20]) # the first anchor point always goes at (0,scale,0)
coord_anchor1 = np.array([0, scale, 0])
dist_origin_anchor1 = distanceBetweenPoints(origin, anchor1)

anchor2 = np.array([30, 20, 10, 20, 40, 30]) # the second anchor always goes at (a2_x, a2_y, 0) with positive a2_x
dist_origin_anchor2 = distanceBetweenPoints(origin, anchor2)
dist_anchor1_anchor2 = distanceBetweenPoints(anchor1, anchor2)
a2_y = (dist_origin_anchor2**2 - dist_anchor1_anchor2**2 + scale**2) / (2*scale)
a2_x = math.sqrt(dist_origin_anchor2**2 - a2_y**2)
coord_anchor2 = np.array([a2_x, a2_y, 0])
print(coord_anchor2)

anchor3 = np.array([20, 10, 0, 10, 30, -20]) # the third anchor goes at (a3_x, a3_y, a3_z) with positive a3_z
# TODO



### Find the coordinates of the 5th point given 4 points and their distances from the 5th point
### Source: https://github.com/akshayb6/trilateration-in-3d/blob/master/trilateration.py 
def trilaterate3D(distances):
    p1=np.array(distances[0][:3])
    p2=np.array(distances[1][:3])
    p3=np.array(distances[2][:3])       
    p4=np.array(distances[3][:3])
    r1=distances[0][-1]
    r2=distances[1][-1]
    r3=distances[2][-1]
    r4=distances[3][-1]
    e_x=(p2-p1)/np.linalg.norm(p2-p1)
    i=np.dot(e_x,(p3-p1))
    e_y=(p3-p1-(i*e_x))/(np.linalg.norm(p3-p1-(i*e_x)))
    e_z=np.cross(e_x,e_y)
    d=np.linalg.norm(p2-p1)
    j=np.dot(e_y,(p3-p1))
    x=((r1**2)-(r2**2)+(d**2))/(2*d)
    y=(((r1**2)-(r3**2)+(i**2)+(j**2))/(2*j))-((i/j)*(x))
    z1=np.sqrt(r1**2-x**2-y**2)
    z2=np.sqrt(r1**2-x**2-y**2)*(-1)
    ans1=p1+(x*e_x)+(y*e_y)+(z1*e_z)
    ans2=p1+(x*e_x)+(y*e_y)+(z2*e_z)
    dist1=np.linalg.norm(p4-ans1)
    dist2=np.linalg.norm(p4-ans2)
    if np.abs(r4-dist1)<np.abs(r4-dist2):
        return ans1
    else: 
        return ans2


