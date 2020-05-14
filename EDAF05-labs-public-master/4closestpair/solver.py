import sys
from math import sqrt

# Read input

n_points = int(sys.stdin.readline())

points = []

for important_variable in range(n_points):
    temp_point = sys.stdin.readline().split()
    points.append((int(temp_point[0]), int(temp_point[1])))

# Sort

p_sorted_x = sorted(points, key=lambda p: p[0])
p_sorted_y = sorted(points, key=lambda p: p[1])


def closest(p_x, p_y, n):

    if n <= 3:
        return min_dist(p_x)

    p_left_x = p_x[:len(p_x)//2]
    p_right_x = p_x[len(p_x)//2:]

    p_left_y = sorted(p_left_x, key=lambda p: p[1])
    p_right_y = sorted(p_right_x, key=lambda p: p[1])

    delta_left = closest(p_left_x, p_left_y, len(p_left_x))
    delta_right = closest(p_right_x, p_right_y, len(p_right_x))

    delta = min(delta_left, delta_right)

    # calc delta from grid

    # coordinate of line
    x_p = (p_left_x[-1][0] + p_right_x[0][0]) / 2

    # choose points within delta of line x_p
    s_y = [p for p in p_y if abs(p[0] - x_p) <= delta]




def min_dist(p_x):
    # distf = lambda p1, p2: sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    if len(p_x) == 3:
        d1 = sqrt((p_x[1][0] - p_x[0][0]) ** 2 + (p_x[1][1] - p_x[0][1]) ** 2)
        d2 = sqrt((p_x[2][0] - p_x[1][0]) ** 2 + (p_x[2][1] - p_x[1][1]) ** 2)
        d3 = sqrt((p_x[0][0] - p_x[2][0]) ** 2 + (p_x[0][1] - p_x[2][1]) ** 2)

        return min(d1,d2,d3)

        # return min([distf(p1, p2) for p1, p2 in zip(p_x, p_x)])
    else:
        # return distf(p_x[0], p_x[1])
        return sqrt((p_x[1][0] - p_x[0][0]) ** 2 + (p_x[1][1] - p_x[0][1]) ** 2)



closest(p_sorted_x, p_sorted_y, n_points)

