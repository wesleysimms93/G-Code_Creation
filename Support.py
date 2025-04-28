
import numpy as np
import math

def next_char(char):
    # Find the next character using the ord() and chr() functions
    return chr(ord(char) + 1)

def unique_number(num1, num2):
    # Ensure the smaller number comes first
    return min(num1, num2) * 10000 + max(num1, num2)

def unique_cord_number(num1, num2):
    # Ensure the smaller number comes first
    return num1 * 10000 + num2


class Point:
    def __init__(self ,x,y,z,name):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.name = int(name)

    def __str__(self):
        return str(self.name)

    def calculate_distance(point1, point2):
    # Calculate the Euclidean distance between two points
        distance = math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)
        return distance


class line_graph:
    def __init__(self):
        self.points = []
        self.edges = {}
        self.x_range = [0, 1]  # Range for X values
        self.y_range = [0, 1]    # Range for Y values
        #self.points.append(Point(0,0,0,1))

    def get_point(self, point_name):
        for point in self.points:
            if point.name == point_name:
                return point
            
    def get_point_remove(self, point_name):
        for point in self.points:
            if point.name == point_name:
                self.points.remove(point)
                return point

    def append_point(self, point):
        self.points.append(point)
        if self.y_range[0] > point.y:
            self.y_range[0] = point.y
        if self.y_range[1] < point.y:
            self.y_range[1] = point.y
        if self.x_range[0] > point.x:
            self.x_range[0] = point.x 
        if self.x_range[1] < point.x:
            self.x_range[1] = point.x
        return
    
    def create_edges(self):
        for point in self.points:
            for point2 in self.points:
                if(point2.name != point.name):
                    unique_numb = unique_number(point2.name , point.name)
                    if (self.edges.get(unique_numb, -1) == -1):
                        #print("Distance Does not exist!")
                        self.edges[unique_numb] = Point.calculate_distance(point, point2)

    def Snake_Sailes_Men(self):
        self.create_edges()
        Flip = False
        left_points = {}
        snake_path = []
        snake_distance = -1 
        for points in self.points:
            left_points[(points.x,points.y)] = points.name
        for i in range(self.x_range[0] -1 ,self.x_range[1] + 1):
            if Flip:
                for j in range(self.y_range[0] - 1,self.y_range[1] + 1):
                 
                    val = left_points.pop((i,j),None)
                    if val != None:
                        
                        snake_path.append(val)
                        if len(left_points) == 0:
                            distance = 0
                            for i in range(len(snake_path) - 1):
                                    unique_numb = unique_number(snake_path[i], snake_path[i + 1])
                                    distance += self.edges.get(unique_numb, float('inf'))
                            return distance, snake_path
                Flip = False
            else:
                for j in reversed(range(self.y_range[0] - 1,self.y_range[1]+ 1)):
                    val = left_points.pop((i,j),None)
                    if val != None:
                        snake_path.append(val)
                        #print((left_points))
                        if len(left_points) == 0:
                            distance = 0
                            for i in range(len(snake_path) - 1):
                                    unique_numb = unique_number(snake_path[i], snake_path[i + 1])
                                    distance += self.edges.get(unique_numb, float('inf'))
                            return distance, snake_path
                Flip = True
        #self.points.pop(0)
        print(f"The following was left behind:{left_points}")
        return -1, []
    

    def Drunk_Snake_Sailes_Men(self):
        self.create_edges()
        Flip = False
        left_points = {}
        snake_path = []
        snake_distance = -1 
        for points in self.points:
            left_points[(points.x,points.y)] = points.name
        for i in reversed(range(self.x_range[0] -1 ,self.x_range[1] + 1)):
            if Flip:
                for j in range(self.y_range[0] - 1,self.y_range[1] + 1):
                 
                    val = left_points.pop((i,j),None)
                    if val != None:
                        
                        snake_path.append(val)
                        if len(left_points) == 0:
                            distance = 0
                            for i in range(len(snake_path) - 1):
                                    unique_numb = unique_number(snake_path[i], snake_path[i + 1])
                                    distance += self.edges.get(unique_numb, float('inf'))
                            return distance, list(reversed(snake_path))
                Flip = False
            else:
                for j in reversed(range(self.y_range[0] - 1,self.y_range[1]+ 1)):
                    val = left_points.pop((i,j),None)
                    if val != None:
                        snake_path.append(val)
                        #print((left_points))
                        if len(left_points) == 0:
                            #self.points.pop(0)
                            distance = 0
                            for i in range(len(snake_path) - 1):
                                    unique_numb = unique_number(snake_path[i], snake_path[i + 1])
                                    distance += self.edges.get(unique_numb, float('inf'))
                            return distance, list(reversed(snake_path))
                Flip = True
        #self.points.pop(0)
        print(f"The following was left behind:{left_points}")
        return -1, []


    def Sorting_Salesmen(self):
        #start_point = Point(0, 0, 0, -1)
        #self.points.insert(0, start_point)
        unique_points = []
        unique_points_dict_name = {}
        for points in self.points:
            point_un = unique_cord_number(points.x,points.y)
            #print(point_un)
            unique_points.append(point_un)
            unique_points_dict_name[point_un] = points.name
        #print(unique_points)
        #print(unique_points_dict_name)
        unique_points = sorted(unique_points)
        output = []
        #print(unique_points)
        for point_numb in unique_points:
            try:
                output.append(unique_points_dict_name[point_numb])
            except:
                #self.points.pop(0)
                return False , []
        #self.points.pop(0)
        distance = 0
        for i in range(len(output) - 1):
                unique_numb = unique_number(output[i], output[i + 1])
                distance += self.edges.get(unique_numb, float('inf'))
        return distance , output


        

   
        return shortest_path, shortest_distance
    def generate_permutations(self, points):
        # Custom function to generate permutations recursively
        def permute(current, remaining, result):
            if not remaining:
                result.append(current)
                #print(current)
                return
            for i in range(len(remaining)):
                permute(current + [remaining[i]], remaining[:i] + remaining[i + 1:], result)

        result = []
        permute([], points, result)
        return result

    def shortest_path(self):
        # Add the starting point (0, 0, 0)
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
       

        return shortest_distance, shortest_path









