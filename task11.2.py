import numpy as np
import matplotlib.pyplot as plt

# set of points to transform
points = np.array([[0, 0, 0],
                   [1, 1, 1],
                   [2, 2, 2],
                   [3, 3, 3],
                   [4, 4, 4]])
# translation transformation values
tx, ty, tz = 3, 4, 5
# rotational transformation values
rx, ry, rz = np.radians([30, 60, 90])

# sine and cosine functions
def s(angle):
    return np.sin(angle)
def c(angle):
    return np.cos(angle)

# get Rx, Ry, and Rz matrices
def get_rotational_x(angle):
    Rx = np.array([[1, 0, 0],
                    [0, c(angle), -s(angle)],
                    [0, s(angle),  c(angle)]])
    return Rx
def get_rotational_y(angle):
    Ry = np.array([[ c(angle), 0, s(angle)],
                    [ 0, 1, 0],
                    [-s(angle), 0, c(angle)]])
    return Ry
def get_rotational_z(angle):
    Rz = np.array([[c(angle), -s(angle), 0],
                    [s(angle),  c(angle), 0],
                    [0, 0, 1]])
    return Rz

# multiply them to get final rotational matrix
def get_rotational(Rx, Ry, Rz):
    return Rz @ Ry @ Rx

# get the transformation matrix my multiplying R and T
def get_htm(R, tx, ty, tz):
    HTM = np.identity(4)
    HTM[0:3, 3] = [tx, ty, tz]
    HTM[0:3, 0:3] = R
    return HTM

# get the result by multiplying the transformation matrix with the points
def get_result(points, HTM):
    points_h = np.hstack([points, np.ones((points.shape[0], 1))])
    result = HTM @ points_h.T
    result = result[:3, :].T
    return result

# get the values
Rx, Ry, Rz = get_rotational_x(rx), get_rotational_y(ry), get_rotational_z(rz)
R = get_rotational(Rx, Ry, Rz)
HTM = get_htm(R, tx, ty, tz)
result = get_result(points, HTM)
print(result)

# --- #

# plotting section

# show the points
ax = plt.figure().add_subplot(111, projection = '3d')
ax.scatter(points[:,0], points[:,1], points[:,2], c='blue', marker='s', label='Original')
ax.scatter(result[:,0], result[:,1], result[:,2], c='red', marker='^', label='Transformed')
# connect the dots with a line
ax.plot(points[:,0], points[:,1], points[:,2], color='blue', alpha=0.5)
ax.plot(result[:,0], result[:,1], result[:,2], color='red', alpha=0.5)

# set labels and show plot
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.show()