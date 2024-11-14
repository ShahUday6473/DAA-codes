import math

# Function to calculate the cost of the solution
def calculate_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]]  # Return to starting city
    return cost

# Function to solve TSP using Branch and Bound
def tsp(graph, n):
    def branch_and_bound(current_bound, current_weight, level, current_path, visited):
        nonlocal min_cost, final_path

        # If all cities are visited, check the total cost including the return to the start
        if level == n:
            total_cost = current_weight + graph[current_path[level - 1]][current_path[0]]
            if total_cost < min_cost:
                final_path = current_path[:level]  # Take only the visited cities
                final_path.append(current_path[0])  # Append starting city at the end
                min_cost = total_cost
                print(f"New minimum cost found: {min_cost} with path: {final_path}")
            return

        for i in range(n):
            if graph[current_path[level - 1]][i] != math.inf and not visited[i]:
                temp_bound = current_bound
                temp_weight = current_weight
                current_weight += graph[current_path[level - 1]][i]

                if level == 1:
                    current_bound -= ((first_min[current_path[level - 1]] + first_min[i]) / 2)
                else:
                    current_bound -= ((second_min[current_path[level - 1]] + first_min[i]) / 2)

                if current_bound + current_weight < min_cost:
                    current_path[level] = i
                    visited[i] = True
                    branch_and_bound(current_bound, current_weight, level + 1, current_path, visited)

                current_weight -= graph[current_path[level - 1]][i]  # Reset weight
                current_bound = temp_bound  # Reset bound
                visited[i] = False

                print(f"Current best cost: {min_cost}, Current path: {final_path}")

    def find_minimums(graph, n):
        first_min = [math.inf] * n
        second_min = [math.inf] * n

        for i in range(n):
            for j in range(n):
                if i != j:
                    if graph[i][j] < first_min[i]:
                        second_min[i] = first_min[i]
                        first_min[i] = graph[i][j]
                    elif graph[i][j] < second_min[i]:
                        second_min[i] = graph[i][j]

        return first_min, second_min

    current_bound = 0
    current_path = [-1] * (n + 1)
    visited = [False] * n

    first_min, second_min = find_minimums(graph, n)
    for i in range(n):
        current_bound += (first_min[i] + second_min[i])
    current_bound = math.ceil(current_bound / 2)

    visited[0] = True
    current_path[0] = 0  # Starting from the first city

    min_cost = math.inf
    final_path = []

    branch_and_bound(current_bound, 0, 1, current_path, visited)

    return min_cost, final_path

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of cities: "))
    graph = []

    print("Enter the cost matrix (use 'inf' for no path):")
    for i in range(n):
        row = input().strip().split()
        graph.append([math.inf if x == 'inf' else int(x) for x in row])

    min_cost, final_path = tsp(graph, n)

    print("Minimum cost:", min_cost)
    print("Path:", final_path)

'''
Why Branch and Bound?
Efficient Search: TSP is a combinatorial optimization problem with a factorial time complexity for brute-force 
solutions, making it computationally expensive for large inputs. Branch and Bound systematically explores paths and 
prunes paths that can’t yield optimal results, reducing the solution space.
Bounding Strategy: By computing lower bounds using minimum edge costs, the algorithm can eliminate many suboptimal 
paths early in the search process.
Optimal Solution: Branch and Bound guarantees finding the optimal solution (unlike heuristic approaches) by 
exhaustively exploring paths within the bounds.
This approach is ideal for TSP when exact solutions are required for small to medium problem sizes, balancing accuracy 
and efficiency through systematic pruning.
'''