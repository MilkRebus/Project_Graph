from math import *


def indent(point, guide, length):
    rad = rad_round(point, guide)
    if length < 0: rad += pi
    return point[0] - length * cos(rad), point[1] + length * sin(rad)


def rad_round(head, guide):
    rad = atan2(guide[1] - head[1], guide[0] - head[0])
    if rad < 0:
        rad = rad * -1 + pi
    else:
        rad = pi - rad
    return rad


def perpendicular_points(cord, height):
    rad = rad_round(cord[0], cord[1])
    first_point = cord[0][0] - height * cos(rad + radians(90)), cord[0][1] + height * sin(rad + radians(90))
    second_point = cord[0][0] - height * cos(rad - radians(90)), cord[0][1] + height * sin(rad - radians(90))
    return first_point, second_point


def triangle_tails(cord, angle_arrow, size_arrow):
    hypotenuse = (size_arrow * tan(radians(angle_arrow / 2)))
    return perpendicular_points(cord, hypotenuse)


def position_simple_arrow(cord, diameter_top, size_arrow):
    cord_first_point = indent(cord[1], cord[0], (diameter_top / 2))
    cord_second_point = indent(cord[0], cord[1], (diameter_top / 2))
    point = indent(cord_first_point, cord_second_point, size_arrow)
    return cord_first_point, cord_second_point, point


def lr_vectors(a, b, center):
    a = (a[0] - center[0], a[1] - center[1])
    b = (b[0] - center[0], b[1] - center[1])
    if a[0] * b[1] - a[1] * b[0] > 0:
        return -1
    else:
        return 1


def comparison(one, two):
    if one < two:
        return -1
    elif one == two:
        return 0
    return 1


def orientation_ratio(head, tail):
    return comparison(head[0], tail[0]), comparison(head[1], tail[1])


def perpendicular_point(cord, height, correct=None):  # cord -> (point, head)
    if correct is None:
        correct = orientation_ratio(cord[0], cord[1])
    rad = rad_round(cord[0], cord[1])
    if 0 in correct:
        correct = correct[::-1]
    return int(cord[0][0] - (cos(rad) * height * correct[0])), int(cord[0][1] + (sin(rad) * height * correct[1]))


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
    depth_first_point = perpendicular_point(
        (indent(cord[0], cord[1], depth_due_arrow), cord[0]), height_due_arrow, correct)
    depth_second_point = perpendicular_point(
        (indent(cord[1], cord[0], depth_due_arrow), cord[0]), height_due_arrow, correct)
    return depth_first_point, depth_second_point


def center_arrow(cord):
    center = (cord[0][0] + cord[1][0]) / 2, (cord[0][1] + cord[1][1]) / 2
    distance = dist(center, cord[0])
    space = distance * (distance / 100)
    return perpendicular_point((center, cord[1]), space)


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


def fun(angle, D):
    if (min(angle) < 0 < max(angle) or min(angle) < 180 < max(angle)) and D > 0:
        return max(angle)
    return min(angle)


def point_on_arc(size_arrow, rad, center, point, guide):
    angle_alpha = asin((size_arrow / (2 * rad))) * 2
    start_chord = degrees(rad_round(point, center))
    correct = lr_vectors(point, guide, center)
    new_angle = start_chord + (angle_alpha * correct)
    return center[0] + rad * cos(new_angle), center[1] - rad * sin(new_angle)


def start_angle(cord, center):
    D = (center[0] - cord[0][0]) * (cord[1][1] - cord[0][1]) - (center[1] - cord[0][1]) * (cord[1][0] - cord[0][0])
    D *= comparison(cord[0][1], cord[1][1])
    angles = (angle_in_round((center, cord[0])), angle_in_round((center, cord[1])))
    return fun(angles, D)
