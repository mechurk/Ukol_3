# coding=utf-8

from abc import ABC, abstractmethod

class GeoJSON(ABC):

    @abstractmethod
    def draw(self):
        pass

class Geometry(GeoJSON):

    def __init__(self, coordinates):
        self.coord = coordinates


class Point(GeoJSON):


    def __init__(self, ax = 0, ay = 0):
        self.x = ax
        self.y = ay

    def __str__(self):
        return "Bod [{} {}]".format(self.x, self.y)

class Polyline(GeoJSON):
    def __init__(self, points):
        self.pts = points

    def __str__(self):
        return "Polyline ({} points)".format(len(self.pts))


class Polygon(GeoJSON):
    def __init__(self, points):
        self.pts = points

    def __str__(self):
        return "Polygon ({} points)".format(len(self.pts))

class LineSegmant(Polyline):
    # Dostane 2 body a medzi nimi vytvorí úsečku
    def __init__(self, p1, p2):
        pts = [p1, p2]
        super().__init__(pts)