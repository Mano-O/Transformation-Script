import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

# set of points to transform
points = np.array([[0, 0, 0],
                   [1, 1, 1],
                   [2, 2, 2],
                   [3, 3, 3],
                   [4, 4, 4]])

# translation transformation values
tx, ty, tz = 3, 4, 5
# rotational transformation values (Euler angles in radians)
rx, ry, rz = np.radians([30, 60, 90])

# convert euler to a quaternion
def euler_to_quaternion(rx, ry, rz):

    cy = np.cos(rz * 0.5)
    sy = np.sin(rz * 0.5)
    cp = np.cos(ry * 0.5)
    sp = np.sin(ry * 0.5)
    cr = np.cos(rx * 0.5)
    sr = np.sin(rx * 0.5)

    qw = cr * cp * cy + sr * sp * sy
    qx = sr * cp * cy - cr * sp * sy
    qy = cr * sp * cy + sr * cp * sy
    qz = cr * cp * sy - sr * sp * cy

    return np.array([qw, qx, qy, qz])

# convert quaternion to rotation
def quaternion_to_rotation_matrix(q):

    qw, qx, qy, qz = q
    R = np.array([
        [1 - 2*qy**2 - 2*qz**2,   2*qx*qy - 2*qz*qw,     2*qx*qz + 2*qy*qw],
        [2*qx*qy + 2*qz*qw,       1 - 2*qx**2 - 2*qz**2, 2*qy*qz - 2*qx*qw],
        [2*qx*qz - 2*qy*qw,       2*qy*qz + 2*qx*qw,     1 - 2*qx**2 - 2*qy**2]
    ])
    return R

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


# Euler to Quaternion
q = euler_to_quaternion(rx, ry, rz)

# uaternion to Rotation Matrix
R = quaternion_to_rotation_matrix(q)

# get HTM (Rotation + Translation)
HTM = get_htm(R, tx, ty, tz)

# Apply to points
result = get_result(points, HTM)
print(result)

#plotting
ax = plt.figure().add_subplot(111, projection = '3d')
ax.scatter(points[:,0], points[:,1], points[:,2], c='blue', marker='s', label='Original')
ax.scatter(result[:,0], result[:,1], result[:,2], c='red', marker='^', label='Transformed')
ax.plot(points[:,0], points[:,1], points[:,2], color='blue', alpha=0.5)
ax.plot(result[:,0], result[:,1], result[:,2], color='red', alpha=0.5)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.show()
