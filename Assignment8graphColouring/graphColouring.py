# Function to check if it is safe to color vertex 'v' with color 'c'
def is_safe(graph, colors, v, c):
    for neighbor in graph[v]:
        if colors[neighbor] == c:  # Check if any adjacent vertex has the same color
            return False
    return True

# Utility function to solve graph coloring problem recursively
def graph_coloring_util(graph, colors, v, color_list):
    # Base case: If all vertices are assigned a color, return True
    if v == len(graph):
        return True
    
    # Try all colors for vertex 'v'
    for c in color_list:
        if is_safe(graph, colors, v, c):
            colors[v] = c  # Assign color 'c' to vertex 'v'
            
            # Recur to assign colors to the rest of the vertices
            if graph_coloring_util(graph, colors, v + 1, color_list):
                return True
            
            # If assigning color 'c' doesn't lead to a solution, remove it (backtrack)
            colors[v] = None
    
    # Return False if no color can be assigned to vertex 'v'
    return False

# Main function to solve the graph coloring problem
def graph_coloring(graph, color_list):
    # Initialize the color assignment list
    colors = [None] * len(graph)
    
    # Solve the graph coloring problem starting from vertex 0
    if not graph_coloring_util(graph, colors, 0, color_list):
        print("Solution does not exist")
    else:
        for i in range(len(graph)):
            print(f"Vertex {i}: {colors[i]}")

# Example graph as an adjacency list
graph = [
    [1, 2, 3],  # Vertex 0 is connected to vertices 1, 2, 3
    [0, 3],      # Vertex 1 is connected to vertices 0, 3
    [0, 3],      # Vertex 2 is connected to vertices 0, 3
    [0, 1, 2]    # Vertex 3 is connected to vertices 0, 1, 2
]

# List of available colors
color_list = ["Red", "Green", "Blue"]

# Solve the graph coloring problem
graph_coloring(graph, color_list)

'''
Why Use Backtracking:
Backtracking is used because:

Exploration of all possibilities: It explores all color assignments for vertices in a systematic manner, ensuring that 
all possible configurations are tried.
Pruning: It stops exploring invalid configurations early by backtracking when it encounters a conflict 
(i.e., two adjacent vertices having the same color).
Efficiency: This avoids unnecessary computation and allows finding the optimal solution in a reasonable amount of time.

'''