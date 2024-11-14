# Function to calculate the maximum value for fractional knapsack
def fractional_knapsack(capacity, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    
    total_value = 0  # Total value accumulated in the knapsack
    item_fractions = []  # List to store fraction of each item added

    # Iterate through sorted items
    for weight, value in items:
        if capacity == 0:
            break  # Stop if the knapsack is full
            
        # Take as much of the item as possible
        if weight <= capacity:
            # If the item can fit fully, take it all
            capacity -= weight
            total_value += value
            item_fractions.append((weight, value, 1))  # Item fully added
        else:
            # Take a fraction of the item to fill the knapsack
            fraction = capacity / weight
            total_value += value * fraction
            item_fractions.append((weight, value, fraction))  # Fraction added
            capacity = 0  # Knapsack is now full

    # Print details
    print("Items and their fractions used:")
    for i, (weight, value, fraction) in enumerate(item_fractions, start=1):
        print(f"Item {i}: weight = {weight}, value = {value}, fraction = {fraction:.2f}")

    return total_value

# List of items (weight, value)
items = [
    (10, 60),  # (weight, value)
    (20, 100),
    (30, 120)
]
capacity = 50  # Total capacity of knapsack

# Calculate and print the maximum value that can be obtained
max_value = fractional_knapsack(capacity, items)
print("Maximum value in the knapsack:", max_value)

'''
### Fractional Knapsack Problem

The **fractional knapsack problem** is a variation of the classic knapsack problem where items can be broken into 
fractions. Given a set of items, each with a weight and a value, the goal is to maximize the total value in a knapsack 
with a fixed capacity. Unlike the 0/1 knapsack problem, where each item must be either taken or left, the fractional 
knapsack allows fractions of items to be taken.

### Greedy Strategy

The **greedy algorithm** is used to solve the fractional knapsack problem by selecting items based on the 
**value-to-weight ratio** (value per unit of weight). The key steps are:

1. **Sort items**: Sort all items by their value-to-weight ratio in **descending order**. This ensures that the items 
providing the most value per unit of weight are considered first.
   
2. **Pick items**: Start picking items in the sorted order:
   - If an item can fit completely in the knapsack, take it all.
   - If an item is too large, take a fraction of it to fill the remaining capacity.

3. **Stop when the knapsack is full**: The process stops when the knapsack is completely filled.

### Why Greedy Works

- The greedy approach works for the fractional knapsack problem because taking the item with the highest 
value-to-weight ratio first maximizes the value at every step. Since we are allowed to take fractions, this ensures 
the optimal solution.

'''
