def compute_weight_table(freq, n):
    # Precompute cumulative frequencies for all ranges
    weight = [[0] * n for _ in range(n)]
    for i in range(n):
        weight[i][i] = freq[i]
        for j in range(i + 1, n):
            weight[i][j] = weight[i][j - 1] + freq[j]
    return weight

def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0] * n for _ in range(n)]  # Cost table
    root = [[0] * n for _ in range(n)]  # Root table
    weight = compute_weight_table(freq, n)

    # Initialize cost for single keys
    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    # Fill tables for larger subtrees
    for length in range(2, n + 1):  # Length of subtree
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            for r in range(i, j + 1):  # Try each key as root
                c = (cost[i][r - 1] if r > i else 0) + (cost[r + 1][j] if r < j else 0) + weight[i][j]
                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r
    return cost, root

def print_tree(keys, root, i, j, parent=None, direction="root"):
    if i > j:
        return
    root_key = keys[root[i][j]]
    print(f"{root_key} is the {direction} child of {parent}" if parent else f"{root_key} is the root")
    print_tree(keys, root, i, root[i][j] - 1, root_key, "left")
    print_tree(keys, root, root[i][j] + 1, j, root_key, "right")

# Get user input
keys = list(map(int, input("Enter keys (space-separated): ").split()))
freq = list(map(int, input("Enter frequencies (space-separated): ").split()))

cost, root = optimal_bst(keys, freq)

print("\nOptimal Binary Search Tree Structure:")
print_tree(keys, root, 0, len(keys) - 1)
