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


# Calculates the minimum distance between any two points recursively
def closest(p_x, p_y, n):

    if n <= 3:
        return min_dist(p_x)

    p_left_x = p_x[:len(p_x)//2]
    p_right_x = p_x[len(p_x)//2:]

    # x-coordinate of line
    x_p = p_left_x[-1][0]

    # Select sorted points by y in r / l half
    p_left_y, p_right_y = [], []

    for point in p_y:

        if point[0] < x_p:
            p_left_y.append(point)
        elif point[0] > x_p:
            p_right_y.append(point)
        # point is on line x_p, place in correct array.
        elif point in p_left_x:
            p_left_y.append(point)
        else:
            p_right_y.append(point)

    # Calc min dist on left and right side
    delta_left = closest(p_left_x, p_left_y, len(p_left_x))
    delta_right = closest(p_right_x, p_right_y, len(p_right_x))

    delta = min(delta_left, delta_right)

    # calc delta from grid

    # choose points within delta of line x_p
    s_y = [p for p in p_y if abs(p[0] - x_p) <= delta]

    # look for points closer than delta within grid
    min_temp = delta

    for i in range(len(s_y)):

        j = i + 1

        while j < len(s_y) and s_y[j][1] - s_y[i][1] < min_temp:

            d = min_dist([s_y[j], s_y[i]])

            if d < min_temp:
                min_temp = d

            j += 1

    return min_temp


# Utility function to calc min dist among 2 or 3 points
def min_dist(p_x):
    if len(p_x) == 3:
        d1 = sqrt((p_x[1][0] - p_x[0][0]) ** 2 + (p_x[1][1] - p_x[0][1]) ** 2)
        d2 = sqrt((p_x[2][0] - p_x[1][0]) ** 2 + (p_x[2][1] - p_x[1][1]) ** 2)
        d3 = sqrt((p_x[0][0] - p_x[2][0]) ** 2 + (p_x[0][1] - p_x[2][1]) ** 2)

        return min(d1, d2, d3)
    else:
        # return distf(p_x[0], p_x[1])
        return sqrt((p_x[1][0] - p_x[0][0]) ** 2 + (p_x[1][1] - p_x[0][1]) ** 2)


closest_dist = closest(p_sorted_x, p_sorted_y, n_points)

print("{:.6f}".format(closest_dist))



