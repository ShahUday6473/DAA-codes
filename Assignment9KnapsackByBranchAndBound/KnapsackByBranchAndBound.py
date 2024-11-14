# Class to represent an item with value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Class to represent a node in the decision tree
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level  # Level of the node in the decision tree
        self.profit = profit  # Total profit so far
        self.weight = weight  # Total weight so far
        self.bound = bound  # Upper bound of the maximum profit in the subtree rooted at this node

# Function to calculate the upper bound of profit for the current node
def calculate_bound(node, n, capacity, items):
    if node.weight >= capacity:
        return 0  # If the weight exceeds capacity, the bound is 0

    # Initialize bound using current profit
    profit_bound = node.profit
    # Start including items from the next level
    j = node.level + 1
    total_weight = node.weight

    # Include items while total weight doesn't exceed capacity
    while j < n and total_weight + items[j].weight <= capacity:
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    # If there's room left in the knapsack, include fraction of the next item
    if j < n:
        profit_bound += (capacity - total_weight) * items[j].value / items[j].weight

    return profit_bound

# Function to solve the 0/1 Knapsack problem using Branch and Bound
def knapsack_branch_and_bound(items, capacity):
    n = len(items)

    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item.value / item.weight, reverse=True)

    # Create a dummy node at level -1
    root = Node(-1, 0, 0, 0)

    # Set the initial bound for the root node
    root.bound = calculate_bound(root, n, capacity, items)

    # Priority queue (max heap) to store live nodes (nodes to be explored)
    queue = []
    queue.append(root)

    # Variable to keep track of the maximum profit found
    max_profit = 0

    while queue:
        # Remove the node with the highest bound from the queue
        current_node = queue.pop(0)

        # Display the current capacity and profit
        print(f"Processing Node: Level {current_node.level}, "
              f"Profit: {current_node.profit}, "
              f"Weight: {current_node.weight}, "
              f"Bound: {current_node.bound}, "
              f"Remaining Capacity: {capacity - current_node.weight}")

        # If this node is promising (its bound is greater than the current max profit)
        if current_node.bound > max_profit and current_node.level < n - 1:
            # Consider the next item (current_node.level + 1)
            next_level = current_node.level + 1

            # Case 1: Include the next item
            left_child = Node(next_level,
                              current_node.profit + items[next_level].value,
                              current_node.weight + items[next_level].weight,
                              0)

            # If the weight is within the capacity, check if this is the best solution
            if left_child.weight <= capacity and left_child.profit > max_profit:
                max_profit = left_child.profit

            # Calculate the bound for this node and add it to the queue if it's promising
            left_child.bound = calculate_bound(left_child, n, capacity, items)
            if left_child.bound > max_profit:
                queue.append(left_child)

            # Case 2: Don't include the next item
            right_child = Node(next_level, current_node.profit, current_node.weight, 0)
            right_child.bound = calculate_bound(right_child, n, capacity, items)

            # Add the right child to the queue if its bound is promising
            if right_child.bound > max_profit:
                queue.append(right_child)

        # Sort the queue by bound in descending order (highest bound first)
        queue.sort(key=lambda node: node.bound, reverse=True)

    return max_profit

def main():
    # Input number of items
    n = int(input("Enter the number of items: "))
    
    # Input items' values and weights
    items = []
    for i in range(n):
        value = int(input(f"Enter value for item {i + 1}: "))
        weight = int(input(f"Enter weight for item {i + 1}: "))
        items.append(Item(value, weight))

    # Input knapsack capacity
    capacity = int(input("Enter the capacity of the knapsack: "))
    
    # Call the knapsack function
    max_profit = knapsack_branch_and_bound(items, capacity)
    print(f"Maximum profit for the knapsack is: {max_profit}")

if __name__ == "__main__":
    main()

'''
Branch and Bound Method
Branch and Bound is a problem-solving technique widely used for combinatorial optimization problems like the 
Knapsack Problem. It systematically explores branches of the solution space, "bounding" (or limiting) further 
exploration based on a calculated upper bound. If a branch can't yield a better solution than the current best, it is 
abandoned, thereby reducing computation.

Application in Knapsack Problem
In the 0/1 Knapsack Problem, we aim to maximize the profit without exceeding a given weight capacity. The Branch and 
Bound algorithm is used here to explore combinations of items to achieve this.
'''