import io 
import datetime as time
import Support
import numpy as np


file = open("./10_points.txt", 'r')

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

file.close()
graph.append_point(Support.Point(0,0,0,-1))
graph.create_edges()

print(f"There are :{len(graph.edges)} edges in the graph")
print(f"The max y is:{graph.y_range[1]}, The min y is:{graph.y_range[0]} ")
print(f"The max x is:{graph.x_range[1]} The min x is:{graph.x_range[0]}")

timestart = time.datetime.now()
# print(f"The Shotest path Brute Salesmen: {graph.shortest_path()}")
# #print(graph.edges)
# timeend = time.datetime.now()    
# print(timeend-timestart)

timestart = time.datetime.now()
dist , Result_list = graph.Snake_Sailes_Men()
print(f"The Shotest path Snake Salesmen: {dist}")
#print(graph.edges)
print("Using Snake")
timeend = time.datetime.now()    
print(timeend-timestart)

timestart = time.datetime.now()
dist2 , Result_list2 = graph.Drunk_Snake_Sailes_Men()
print(f"The Shotest path drunk Snake Salesmen: {dist2}")
#print(graph.edges)
timeend = time.datetime.now()  
if dist2 < dist:
    dist = dist2
    Result_list = Result_list2
    print("Using Drunk Snake")


timestart = time.datetime.now()
dist3 , Result_list3 = graph.Sorting_Salesmen()
print(f"The Shotest path Sorting Salesmen: {dist3}")
#print(graph.edges)
timeend = time.datetime.now()  

if dist3 < dist:
    dist = dist3
    Result_list = Result_list3
    print("Using Sort")


print(timeend-timestart)
with open("gcodetest.txt", "w") as f:
    for element in Result_list:
        point = graph.get_point_remove(element)
        f.write(f"5M X{point.x} Y{point.y} Z{point.z}\n")
print("Write Complete")


