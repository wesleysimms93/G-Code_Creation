
import numpy as np
import math

def next_char(char):
    # Find the next character using the ord() and chr() functions
    return chr(ord(char) + 1)

def unique_number(num1, num2):
    # Ensure the smaller number comes first
    return min(num1, num2) * 10000 + max(num1, num2)



class Point:
    def __init__(self ,x,y,z,name):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.name = int(name)

    def calculate_distance(point1, point2):
    # Calculate the Euclidean distance between two points
        distance = math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2 + (point2.z - point1.z)**2)
        return distance


class line_graph:
    def __init__(self):
        self.points = []
        self.edges = {}
        #self.points.append(Point(0,0,0,1))

    def append_point(self, point):
        self.points.append(point)
        return
    
    def create_edges(self):
        for point in self.points:
            for point2 in self.points:
                if(point2.name != point.name):
                    unique_numb = unique_number(point2.name , point.name)
                    if (self.edges.get(unique_numb, -1) == -1):
                        print("Distance Does not exist!")
                        self.edges[unique_numb] = Point.calculate_distance(point, point2)

    def Solve_The_Problem(self):
        shortest_path = None
        shortest_distance = float('inf')
        def permute(current, remaining, shortest_path, shortest_distance):
            if not remaining:
                #print(current)
                perm = [-1] + current
                distance = 0
                for i in range(len(perm) - 1):
                    unique_numb = unique_number(perm[i], perm[i + 1])
                    distance += self.edges.get(unique_numb, float('inf'))
                if distance < shortest_distance:
                    shortest_distance = distance
                    shortest_path = perm    
                    #print("I Found the Short Path")
                return
            for i in range(len(remaining)):
                permute(current + [remaining[i]], remaining[:i] + remaining[i + 1:], shortest_path ,shortest_distance)

        # Add the starting point (0, 0, 0)
        start_point = Point(0, 0, 0, -1)
        point_names = [ point.name for point in self.points]
        end = []
        self.points.insert(0, start_point)
        self.create_edges()
        # Generate permutations excluding the starting point
        permutations = permute([], point_names, end, shortest_path ,shortest_distance)
        # Check each permutation
        # Add the starting point to the permutation

        return shortest_path, shortest_distance
    def generate_permutations(self, points):
        # Custom function to generate permutations recursively
        def permute(current, remaining, result):
            if not remaining:
                result.append(current)
                print(current)
                return
            for i in range(len(remaining)):
                permute(current + [remaining[i]], remaining[:i] + remaining[i + 1:], result)

        result = []
        permute([], points, result)
        return result

    def shortest_path(self):
        # Add the starting point (0, 0, 0)
        start_point = Point(0, 0, 0, -1)
        self.points.insert(0, start_point)
        self.create_edges()
        # Generate permutations excluding the starting point
        point_names = [point.name for point in self.points if point.name != -1]
        permutations = self.generate_permutations(point_names)

        shortest_path = None
        shortest_distance = float('inf')

        # Check each permutation
        # Add the starting point to the permutation
        for perm in permutations:
            perm = [-1] + perm
            distance = 0
            for i in range(len(perm) - 1):
                unique_numb = unique_number(perm[i], perm[i + 1])
                distance += self.edges.get(unique_numb, float('inf'))

        # Update if this path is shorter
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = perm

        # Remove the starting point from the list to keep data consistent
        self.points.pop(0)

        return shortest_path, shortest_distance









