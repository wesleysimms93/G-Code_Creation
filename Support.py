
import numpy as np
import math


class Point:
    def __init__(self ,x,y,z,name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

    def distance(self, point):
        try:
            return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2 + (self.z - point.z)**2)
        except:
            return -1 

class line_graph:
    def __init__(self):
        self.points = []
        self.edges = {}

    def append_point(self, point):
        self.points.append(Point(point))
        return
    
    def create_edges(self):
        for point in self.points:
            for point2 in self.point:


