import io
import datetime as time
import Support
import numpy as np
import sys  # Import sys to handle command-line arguments

def process_gcode_file(input_filename):
    # Open the input file
    with open(input_filename, 'r') as file:
        char = 1
        graph = Support.line_graph()

        for line in file:
            line = line.replace('(', '').replace(')', '')
            values = line.split(',')
            New_Point = Support.Point(values[0], values[1], values[2], char)
            graph.append_point(New_Point)
            char += 1

    graph.append_point(Support.Point(0, 0, 0, -1))
    graph.create_edges()

    print(f"There are :{len(graph.edges)} edges in the graph")
    print(f"The max y is:{graph.y_range[1]}, The min y is:{graph.y_range[0]} ")
    print(f"The max x is:{graph.x_range[1]} The min x is:{graph.x_range[0]}")

    # Run Snake Salesmen algorithm
    timestart = time.datetime.now()
    dist, Result_list = graph.Snake_Sailes_Men()
    print(f"The Shortest path Snake Salesmen: {dist}")
    print("Using Snake")
    timeend = time.datetime.now()
    print(timeend - timestart)

    # Run Drunk Snake Salesmen algorithm
    timestart = time.datetime.now()
    dist2, Result_list2 = graph.Drunk_Snake_Sailes_Men()
    print(f"The Shortest path Drunk Snake Salesmen: {dist2}")
    timeend = time.datetime.now()
    if dist2 < dist:
        dist = dist2
        Result_list = Result_list2
        print("Using Drunk Snake")

    # Run Sorting Salesmen algorithm
    timestart = time.datetime.now()
    dist3, Result_list3 = graph.Sorting_Salesmen()
    print(f"The Shortest path Sorting Salesmen: {dist3}")
    timeend = time.datetime.now()
    if dist3 < dist:
        dist = dist3
        Result_list = Result_list3
        print("Using Sort")
    print(timeend - timestart)

    # Create the output filename based on the input filename
    output_filename = input_filename.split('.')[0] + "_gcode.txt"

    # Write the results to the output file
    with open(output_filename, "w") as f:
        for element in Result_list:
            point = graph.get_point_remove(element)
            f.write(f"M10 X{point.x} Y{point.y} Z{point.z}\n")
    print("Write Complete")

# Get the input filename from the first argument
if len(sys.argv) < 2:
    print("Usage: python Main.py <input_filename>")
    sys.exit(1)

input_filename = sys.argv[1]

# Process the gcode file
process_gcode_file(input_filename)


