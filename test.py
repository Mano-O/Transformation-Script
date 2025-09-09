import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.transform import Rotation as R

# Original points
points = np.array([[1, 4, 2],
                   [2, 1, 2],
                   [5, 6, 3]])

# Translation
tx, ty, tz = 3, 4, 5

# Rotation angles (degrees)
theta_x, theta_y, theta_z = 30, 60, 90

# ---- Create Quaternion from Euler angles ----
# 'xyz' means rotations applied in x, then y, then z order
rotation = R.from_euler('xyz', [theta_x, theta_y, theta_z], degrees=True)

# Get quaternion (optional: just for inspection)
quat = rotation.as_quat()  # [x, y, z, w]
print("Quaternion (x, y, z, w):", quat)

# ---- Apply Rotation using Quaternion ----
rotated_points = rotation.apply(points)

# ---- Apply Translation ----
transformed_points = rotated_points + np.array([tx, ty, tz])

print("Transformed points:\n", transformed_points)