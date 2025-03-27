import random

def generate_points(N, X_range, Y_range, Z_range, file_name):
    with open(file_name, 'w') as file:
        for _ in range(N):
            # Generate random integer values for x, y, and z within the specified ranges
            x = random.randint(X_range[0], X_range[1])
            y = random.randint(Y_range[0], Y_range[1])
            z = random.randint(Z_range[0], Z_range[1])
            
            # Write the point to the file in the format (x,y,z)
            file.write(f"({x},{y},{z})\n")

# Parameters
N = 4  # Number of points
#X_range = (1, 7924)  # Range for X values
#Y_range = (1, 1524)    # Range for Y values
#Z_range = (1, 914)    # Range for Z values

X_range = (1, 24)  # Range for X values
Y_range = (1, 14)    # Range for Y values
Z_range = (1, 14)    # Range for Z values
file_name = f'{N}_points.txt'  # Output file name

# Generate and save the points
generate_points(N, X_range, Y_range, Z_range, file_name)

print(f"{N} integer points have been written to {file_name}")