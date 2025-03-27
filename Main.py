import io 
import datetime as time
import Support
import numpy as np


file = open("./10_points.txt", 'r')

char = 1

graph = Support.line_graph()

for line in file:
    print(line)
    line = line.replace('(','')
    line = line.replace(')','')
    print(line)
    values = line.split(',')
    New_Point = Support.Point(values[0],values[1],values[2],char)
    graph.append_point(New_Point)
    char += 1
timestart = time.datetime.now()
print(f"The Shotest path: {graph.shortest_path()}")
print(graph.edges)
print(f"There are :{len(graph.edges)} edges in the graph")
timeend = time.datetime.now()    
print(timeend-timestart)
