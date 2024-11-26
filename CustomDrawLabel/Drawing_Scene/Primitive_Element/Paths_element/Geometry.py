from math import *


def distance(first_point, second_point):
    return sqrt((first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2)


def center_segment(cord):
    return (cord[0][0] + cord[1][0]) / 2, (cord[0][1] + cord[1][1]) / 2


def radian_segment(cord_segment):
    if cord_segment[1][0] - cord_segment[0][0] == 0:
        return radians(90)
    return atan((cord_segment[1][1] - cord_segment[0][1]) / (cord_segment[1][0] - cord_segment[0][0]))


def comparison(one, two):
    if one < two:
        return -1
    elif one == two:
        return 0
    return 1


def orientation_ratio(head, tail):
    return comparison(head[0], tail[0]), comparison(head[1], tail[1])


def cathets_displacement(hypotenuse, radian):
    y = abs(hypotenuse * sin(radian))
    x = abs(hypotenuse * cos(radian))
    return (x, y)


def indent(head, tail, dist):
    ratio = orientation_ratio(head, tail)
    radian = radian_segment([head, tail])
    cathets = cathets_displacement(dist, radian)
    return (
        int(head[0] - (cathets[0] * ratio[0])),
        int(head[1] - (cathets[1] * ratio[1]))
    )


def max_y(one, two):
    if one[1] > two[1]:
        return one
    else:
        return two


def min_y(one, two):
    if one[1] < two[1]:
        return one
    else:
        return two


def orientation_arrow(cord):
    maxy = max_y(cord[0], cord[1])
    miny = min_y(cord[0], cord[1])
    if maxy[0] > miny[0]:
        return [1, -1]
    else:
        return [-1, 1]


def triangle_tails(cord, angle_arrow, size_arrow):
    hypotenuse = (size_arrow * tan(radians(angle_arrow / 2)))
    return perpendicular_points(cord, hypotenuse)


def position_simple_arrow(cord, diameter_top, size_arrow):
    cord_first_point = indent(cord[1], cord[0], (diameter_top / 2))
    cord_second_point = indent(cord[0], cord[1], (diameter_top / 2))
    point = indent(cord_first_point, cord_second_point, size_arrow)
    return cord_first_point, cord_second_point, point


def perpendicular_points(cord, height):
    correct = orientation_arrow(cord)
    radian = radian_segment(cord)
    cathets = cathets_displacement(height, radian)
    first_point = (int(cord[0][0] + cathets[1]), int(cord[0][1] - (cathets[0] * correct[0])))
    second_point = (int(cord[0][0] - cathets[1]), int(cord[0][1] - (cathets[0] * correct[1])))
    return first_point, second_point


def perpendicular_point_only(cord, height, correct=None):  # cord -> (point, head)
    if correct is None:
        correct = orientation_ratio(cord[0], cord[1])
    radian = radian_segment(cord)
    cathets = cathets_displacement(height, radian)
    if 0 in correct:
        correct = correct[::-1]
    return int(cord[0][0] - (cathets[1] * correct[0])), int(cord[0][1] + (cathets[0] * correct[1]))


def angle_for_round(cord):
    if cord[0][0] - cord[1][0] == 0:
        if cord[0][1] < cord[1][1]:
            return 90
        return -90
    else:
        return degrees(atan((cord[0][1] - cord[1][1]) / (cord[0][0] - cord[1][0])))


def angle_in_round(cord):
    angle = angle_for_round(cord)
    if cord[0][0] > cord[1][0]:
        angle = 180 - angle
    else:
        if angle <= 0:
            angle = 0 - angle
        else:
            angle = 360 - angle
    return angle


def angle_for_chord(cord):
    angle = angle_for_round(cord)
    if cord[0][0] > cord[1][0]:
        if angle < 0:
            angle = 0 - angle
        else:
            angle = 360 - angle
    else:
        angle = 180 - angle
    return radians(angle)


def fun(angle, D):
    if (min(angle) < 0 < max(angle) or min(angle) < 180 < max(angle)) and D > 0:
        return max(angle)
    return min(angle)


def start_angle(cord, center):
    D = (center[0] - cord[0][0]) * (cord[1][1] - cord[0][1]) - (center[1] - cord[0][1]) * (cord[1][0] - cord[0][0])
    D *= comparison(cord[0][1], cord[1][1])
    angles = (angle_in_round((center, cord[0])), angle_in_round((center, cord[1])))
    return fun(angles, D)


def center_arrow(cord):
    center = center_segment(cord)
    dist = distance(center, cord[0])
    space = dist * (dist / 100)
    return perpendicular_point_only((center, cord[1]), space)


def left_right_vectors(a, b, center):
    a = (a[0] - center[0], a[1] - center[1])
    b = (b[0] - center[0], b[1] - center[1])
    if a[0] * b[1] - a[1] * b[0] > 0:
        return -1
    else:
        return 1


def degrees_by_point(a, b, c):
    ac = ((c[0] - a[0]), (c[1] - a[1]))
    bc = ((c[0] - b[0]), (c[1] - b[1]))
    ac_dist = sqrt(ac[0] ** 2 + ac[1] ** 2)
    bc_dist = sqrt(bc[0] ** 2 + bc[1] ** 2)
    scal = (ac[0] * bc[0]) + (ac[1] * bc[1])
    deg = acos(scal / (ac_dist * bc_dist))
    return degrees(deg)


def points_between_top(cord, depth_due_arrow, height_due_arrow):
    correct = orientation_ratio(cord[1], cord[0])
    depth_first_point = perpendicular_point_only(
        (indent(cord[0], cord[1], depth_due_arrow), cord[0]), height_due_arrow, correct)
    depth_second_point = perpendicular_point_only(
        (indent(cord[1], cord[0], depth_due_arrow), cord[0]), height_due_arrow, correct)
    return depth_first_point, depth_second_point


def point_on_arc(size_arrow, rad, center, point, guide):
    angle_alpha = asin((size_arrow / (2 * rad))) * 2
    start_chord = angle_for_chord((point, center))
    correct = left_right_vectors(point, guide, center)
    new_angle = start_chord + (angle_alpha * correct)
    return center[0] + rad * cos(new_angle), center[1] - rad * sin(new_angle)


def height_arc_segment(between, center):
    rad = distance(between[0], center)
    return rad - sqrt(rad ** 2 - (dist(between[0], between[1]) / 2) ** 2)


def angle_text(cord):
    angle = angle_for_round(cord)
    if angle < 0:
        return 360 + angle
    return angle
