import numpy as np

points = np.array([[1, 4, 2],
                   [2, 1, 2],
                   [5, 6, 3]])
tx, ty, tz = 3, 4, 5
rx, ry, rz = np.radians([30, 60, 90])

def s(angle):
    return np.sin(angle)
def c(angle):
    return np.cos(angle)

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

def get_rotational(Rx, Ry, Rz):
    return Rz @ Ry @ Rx

def get_htm(R, tx, ty, tz):
    HTM = np.identity(4)
    HTM[0:3, 3] = [tx, ty, tz]
    HTM[0:3, 0:3] = R
    return HTM

def get_result(points, HTM):
    points_h = np.hstack([points, np.ones((points.shape[0], 1))])
    result = HTM @ points_h.T
    result = result[:3, :].T
    return result

Rx, Ry, Rz = get_rotational_x(rx), get_rotational_y(ry), get_rotational_z(rz)
R = get_rotational(Rx, Ry, Rz)
HTM = get_htm(R, tx, ty, tz)
result = get_result(points, HTM)
print(result)
