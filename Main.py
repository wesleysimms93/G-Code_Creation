import io 
import time 
import Support
import numpy as np


file = open("./text.txt", 'r')


graph = []

for line in file:
    print(line)
    line.replace('(','')
    line.replace(')','')
    values = line.split(',')
    graph.append(Support.Point(values[0],values[1],values[2]))

print(graph)



    

