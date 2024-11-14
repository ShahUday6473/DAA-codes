def knapsack(weights, values, W, n):
    # Create a DP table with dimensions (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(n + 1):
        for w in range(W + 1):
            # If no items or weight capacity is 0, the value is 0
            if i == 0 or w == 0:
                dp[i][w] = 0
            # If the weight of the current item is less than or equal to the capacity
            elif weights[i - 1] <= w:
                # Max of including the current item or excluding it
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Exclude the current item
                dp[i][w] = dp[i - 1][w]
    
    # Print the DP table in a readable format
    print_dp_table(dp, n, W)
    
    # The result will be in the bottom-right corner of the DP table
    return dp[n][W]

def print_dp_table(dp, n, W):
    print("DP Table:")
    print(" " * 6, end="")  # Print space for the row header
    for w in range(W + 1):
        print(f"{w:3}", end=" ")  # Print weight capacities header
    print()
    
    for i in range(n + 1):
        if i == 0:
            print(" 0 ", end="")  # Row header for no items
        else:
            print(f"{i:2}", end=" ")  # Row header for item number
        for w in range(W + 1):
            print(f"{dp[i][w]:3}", end=" ")  # Print each cell in the table
        print()

values = [2,4,7,10]  # Values of the items
weights = [1,3,5,7]   # Weights of the items
W = 8                   # Capacity of the knapsack
n = len(values)          # Number of items
    
result = knapsack(weights, values, W, n)
print(f"Maximum value that can be obtained: {result}")

'''
### Dynamic Programming (DP) in Short:
Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It 
solves each subproblem just once and stores the results (usually in a table) to avoid redundant work. DP is used when 
a problem has **overlapping subproblems** and **optimal substructure**, meaning the solution to the problem can be 
constructed efficiently from solutions to its subproblems.

### 0/1 Knapsack Problem Using Dynamic Programming:
The **0/1 Knapsack Problem** is a combinatorial optimization problem where:
- Given a set of items, each with a weight and a value, and a knapsack with a fixed capacity, the goal is to determine 
the maximum value that can be obtained by including a subset of the items in the knapsack without exceeding its weight 
capacity.

#### Steps for Solving 0/1 Knapsack Using DP:
1. **Define the DP Table**: 
   - Let `dp[i][w]` represent the maximum value that can be obtained using the first `i` items and a knapsack capacity 
   `w`.
   - The table has dimensions `(n+1)` x `(W+1)`, where `n` is the number of items, and `W` is the knapsack's capacity.

2. **Base Case**: 
   - When there are no items (`i=0`) or the capacity is zero (`w=0`), the value is zero: `dp[0][w] = 0` and 
   `dp[i][0] = 0`.

3. **Recurrence Relation**:
   - If the weight of the current item `weights[i-1]` is less than or equal to the current capacity `w`, we have two 
   choices:
     1. **Include the item**: The value will be `values[i-1] + dp[i-1][w-weights[i-1]]`.
     2. **Exclude the item**: The value will be `dp[i-1][w]`.
   - Take the maximum of these two options:
     dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]])

   - If the current item’s weight is greater than the remaining capacity, we exclude the item:
     dp[i][w] = dp[i-1][w]

4. **Result**: 
   - After filling the table, the maximum value is found in `dp[n][W]`, where `n` is the number of items, and `W` is the knapsack's capacity.

### Using DP to Solve the 0/1 Knapsack Problem Efficiently:
The key idea in DP is to **reuse solutions** to smaller subproblems. Instead of recomputing values repeatedly, DP 
stores intermediate results, making the solution more efficient than brute force methods. The time complexity of the 
DP approach for the 0/1 Knapsack problem is **O(n * W)**, where `n` is the number of items and `W` is the knapsack 
capacity.

def print_dp_table(dp, n, W):
    print("DP Table:")
    print(" " * 6, end="")  # Print space for the row header
    for w in range(W + 1):
        print(f"{w:3}", end=" ")  # Print weight capacities header
    print()
    
    for i in range(n + 1):
        if i == 0:
            print(" 0 ", end="")  # Row header for no items
        else:
            print(f"{i:2}", end=" ")  # Row header for item number
        for w in range(W + 1):
            print(f"{dp[i][w]:3}", end=" ")  # Print each cell in the table
        print()
'''