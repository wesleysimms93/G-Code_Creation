import matplotlib.pyplot as plt
from Support import line_graph, Point


def visualize_graph(graph, path, graph_edges = False):
    # Create a plot
    plt.figure(figsize=(10, 10))

    # Plot points
    for point in graph.points:
        plt.scatter(point.x, point.y, label=f"Point {point.name}")
        plt.text(point.x, point.y, f"{point.name}", fontsize=9, ha='right')
    if graph_edges:
    # Plot edges
        for (key, distance) in graph.edges.items():
            # Extract points from unique key
            point1_name, point2_name = divmod(key, 10000)
            point1 = next(p for p in graph.points if p.name == point1_name)
            point2 = next(p for p in graph.points if p.name == point2_name)

        plt.plot([point1.x, point2.x], [point1.y, point2.y], 'b--')  # Dashed blue lines for edges
    for i in range(len(path) - 1):
            point1 = next(p for p in graph.points if p.name == path[i])
            point2 = next(p for p in graph.points if p.name == path[i + 1])
            plt.plot([point1.x, point2.x], [point1.y, point2.y], 'g-', label="Snake Path")



    # Add titles and labels
    plt.title("Graph Visualization")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.legend()
    plt.draw()


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
    New_Point = Point(values[0],values[1],values[2],char)
    graph.append_point(New_Point)
    char += 1
graph.append_point(Point(0,0,0,-1))
graph.create_edges()

bool_result , Result_list = graph.shortest_path()
print(Result_list)
visualize_graph(graph,Result_list)

bool_result , Result_list = graph.Snake_Sailes_Men()
visualize_graph(graph,Result_list)

bool_result , Result_list = graph.Sorting_Salesmen()
visualize_graph(graph,Result_list)

plt.show()