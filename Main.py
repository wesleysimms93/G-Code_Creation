import io 
import datetime as time
import Support
import numpy as np


file = open("./4_points.txt", 'r')

char = 1

graph = Support.line_graph()

for line in file:
    #print(line)
    line = line.replace('(','')
    line = line.replace(')','')
    #print(line)
    values = line.split(',')
    New_Point = Support.Point(values[0],values[1],values[2],char)
    graph.append_point(New_Point)
    char += 1


print(f"There are :{len(graph.edges)} edges in the graph")
print(f"The max y is:{graph.y_range[1]}, The min y is:{graph.y_range[0]} ")
print(f"The max x is:{graph.x_range[1]} The min x is:{graph.x_range[0]}")
timestart = time.datetime.now()
print(f"The Shotest path Brute Salesmen: {graph.shortest_path()}")
#print(graph.edges)
timeend = time.datetime.now()    
print(timeend-timestart)

timestart = time.datetime.now()
print(f"The Shotest path Snake Salesmen: {graph.Snake_Sailes_Men()}")
#print(graph.edges)
timeend = time.datetime.now()    
print(timeend-timestart)

timestart = time.datetime.now()
print(f"The Shotest path Sorting Salesmen: {graph.Sorting_Salesmen()}")
#print(graph.edges)
timeend = time.datetime.now()  

print(timeend-timestart)


