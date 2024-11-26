from math import dist
from math import sqrt

from PyQt6.QtCore import QRectF, QPointF
from PyQt6.QtGui import QPainterPath, QPolygonF, QFont

from Config import *
from .Geometry import *


class ArcPath(QPainterPath):
    def __init__(self, cord):
        super(ArcPath, self).__init__()
        self.between = points_between_top(cord, depth_due_arrow, sqrt(radius_top ** 2 - depth_due_arrow ** 2))
        self.center = center_arrow(cord)

        self.rad = dist(self.center, self.between[0])

        point = point_on_arc(size_arrow, self.rad, self.center, self.between[1], self.between[0])
        rectangle = QRectF(self.center[0] - self.rad, self.center[1] - self.rad, self.rad * 2, self.rad * 2)
        startAngle = start_angle((point, self.between[0]), self.center)
        spanAngle = degrees_by_point(point, self.between[0], self.center)

        self.arcMoveTo(rectangle, startAngle)
        self.arcTo(rectangle, startAngle, spanAngle)
        self.addPath(PathTriangle(self.between[1], point))


class ArrowPath(QPainterPath):
    def __init__(self, cord):
        super(ArrowPath, self).__init__()
        self.cord = position_simple_arrow(cord, diameter_top, size_arrow)
        self.moveTo(self.cord[1][0], self.cord[1][1])
        self.lineTo(self.cord[2][0], self.cord[2][1])
        self.addPath(PathTriangle(self.cord[0], self.cord[2]))


class LoopPath(QPainterPath):
    def __init__(self, cord):
        super(LoopPath, self).__init__()
        dist = ((radius_top ** 2 + joint ** 2 - radius_loop ** 2) / (2 * radius_top * joint)) * radius_top
        height = sqrt(radius_top ** 2 - dist ** 2)
        self.center = indent(cord[0], cord[1], joint)
        j = indent(cord[0], cord[1], dist)
        self.between = perpendicular_points((j, cord[0]), height)

        point = point_on_arc(size_arrow * -1, radius_loop, self.center, self.between[1], self.between[0])
        rectangle = QRectF(self.center[0] - radius_loop, self.center[1] - radius_loop, radius_loop * 2, radius_loop * 2)
        startAngle = start_angle((point, self.between[0]), self.center)
        spanAngle = -360 + degrees_by_point(point, self.between[0], self.center)

        self.arcMoveTo(rectangle, startAngle)
        self.arcTo(rectangle, startAngle, spanAngle)
        self.addPath(PathTriangle(self.between[1], point))


class StickPath(QPainterPath):
    def __init__(self, cord):
        super(StickPath, self).__init__()
        self.cord = cord
        cord = self.position_stick()
        self.moveTo(cord[0][0], cord[0][1])
        self.lineTo(cord[1][0], cord[1][1])

    def position_stick(self):
        cord_first_point = indent(self.cord[0], self.cord[1], (diameter_top / 2))
        cord_second_point = indent(self.cord[1], self.cord[0], (diameter_top / 2))
        return [cord_first_point, cord_second_point]


class TopPath(QPainterPath):
    def __init__(self, cord):
        super(TopPath, self).__init__()
        self.cord = cord
        #self.font = QFont()
        self.addEllipse(cord[0] - diameter_top / 2, cord[1] - diameter_top / 2, diameter_top, diameter_top)


class PathTriangle(QPainterPath):
    def __init__(self, head, point):
        super(PathTriangle, self).__init__()
        tail_arrow = triangle_tails((point, head), angle_arrow, size_arrow + (diameter_top / 2))
        points = QPolygonF(
            [QPointF(tail_arrow[1][0], tail_arrow[1][1]), QPointF(point[0], point[1]),
             QPointF(tail_arrow[0][0], tail_arrow[0][1]),
             QPointF(head[0], head[1]), QPointF(tail_arrow[1][0], tail_arrow[1][1])])
        self.addPolygon(points)
