import math


def check_line_overlap(l1, l2):
    if l1 == l2:
        return False

    l1_slope = calculate_line_slope(l1)
    l2_slope = calculate_line_slope(l2)

    slope_almost_equals = math.isclose(l1_slope, l2_slope, rel_tol=0.001)
    return not slope_almost_equals


def calculate_line_slope(line):
    p1 = line[0]
    p2 = line[1]

    delta_x = p1[0] - p2[0]
    delta_y = p1[1] - p2[1]

    if delta_y == 0:
        return math.inf
    return delta_x / delta_y

