# coding=utf-8

from abc import ABC, abstractmethod


class GeoJson(ABC):
    pass

    # @abstractmethod
    # def bbox (self):
    #   pass


class Feature(GeoJson):
    def __init__(self, id, geometry):
        self.id = id
        self.geometry = geometry


class FeatureCollection(GeoJson):
    def __init__(self, features):
        self.features = features


class Geometry(GeoJson, ABC):
    pass


class GeometryCollection(Geometry):
    def __init__(self, geometries):
        self.geometries = geometries


class Point(Geometry):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point [{} {}]".format(self.x, self.y)


class LineString(Geometry):
    def __init__(self, points):
        self.points = points

    def __str__(self):
        return "Linestring ({} points)".format(len(self.points))


class Polygon(Geometry):
    def __init__(self, exterior_ring, interior_rings):
        self.exteriorRing = exterior_ring
        self.interiorRings = interior_rings


class MultiGeometry(Geometry, ABC):
    """Abstraktní třída, potomek třídy geometry,
    vytvořena pro metodu explode geometry """
    def __init__(self, multi_geometries):
        self.multi_geometries = multi_geometries

    def explode(self):
        return self.multi_geometries


class MultiPoint(MultiGeometry):
    def __init__(self, points):
        super().__init__(points)


class MultiLineString(MultiGeometry):
    def __init__(self, line_strings):
        super().__init__(line_strings)


class MultiPolygon(MultiGeometry):
    def __init__(self, polygons):
        super().__init__(polygons)
