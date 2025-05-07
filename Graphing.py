import matplotlib.pyplot as plt
from Support import line_graph, Point
import Support
import time
import datetime as time

def visualize_graph(graph, path, total_distance, Title="Graph", graph_edges=False):
    # Create a plot
    plt.figure(figsize=(10, 10))

    # Plot points
    for point in graph.points:
        plt.scatter(point.x, point.y, label=f"Point {point.name}")
        plt.text(point.x, point.y, f"{point.name}", fontsize=9, ha='right')

    # Plot edges if enabled
    if graph_edges:
        for (key, distance) in graph.edges.items():
            # Extract points from unique key
            point1_name, point2_name = divmod(key, 10000)
            point1 = next(p for p in graph.points if p.name == point1_name)
            point2 = next(p for p in graph.points if p.name == point2_name)
            plt.plot([point1.x, point2.x], [point1.y, point2.y], 'b--')  # Dashed blue lines for edges

    # Plot the path
    if path:
        for i in range(len(path) - 1):
            point1 = next(p for p in graph.points if p.name == path[i])
            point2 = next(p for p in graph.points if p.name == path[i + 1])
            plt.plot([point1.x, point2.x], [point1.y, point2.y], 'g-', label="Path" if i == 0 else "")  # Add label only once

    # Add titles and labels
    plt.title(f"{Title} Visualization (Total Distance: {total_distance})")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.legend()
    #plt.show()


# Example usage
graph = line_graph()
file = open("./10_points.txt", 'r')
char = 1
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
graph.create_edges()
dist , Result_list = graph.Snake_Sailes_Men()
print(f"The Shotest path Snake Salesmen: {dist}")
#print(graph.edges)
print("Using Snake")
visualize_graph(graph,Result_list, dist, "Snake")
timestart = time.datetime.now()
dist2 , Result_list2 = graph.Drunk_Snake_Sailes_Men()
print(f"The Shotest path drunk Snake Salesmen: {dist2}")
#print(graph.edges)
#print(Result_list2)
visualize_graph(graph,Result_list2, dist2, "Drunk Snake")
dist3 , Result_list3 = graph.Sorting_Salesmen()
print(f"The Shotest path Sorting Salesmen: {dist3}")
dist , Result_list = graph.Sorting_Salesmen()
visualize_graph(graph,Result_list, dist,"Sorting")
print(Result_list)
plt.show()