class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# Function to calculate the frequency of each character in the string
def calculate_frequency(data):
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Function to build the Huffman Tree
def build_huffman_tree(frequency):
    nodes = [Node(char, freq) for char, freq in frequency.items()]
    
    while len(nodes) > 1:
        # Sort nodes based on frequency
        nodes.sort(key=lambda x: x.freq)

        # Pick two nodes with the lowest frequency
        left = nodes.pop(0)
        right = nodes.pop(0)

        # Create a new internal node with these two nodes as children
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the new node back to the list of nodes
        nodes.append(merged)
    
    return nodes[0]  # The remaining node is the root of the Huffman Tree

# Function to generate Huffman codes from the Huffman Tree
def generate_codes(node, current_code, codes):
    if node is None:
        return
    
    # If the node is a leaf node, add the code to the dictionary
    if node.char is not None:
        codes[node.char] = current_code
    
    # Traverse the left and right children with updated codes
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

# Main function to encode data using Huffman Encoding
def huffman_encoding(data):
    frequency = calculate_frequency(data)
    root = build_huffman_tree(frequency)
    codes = {}
    generate_codes(root, "", codes)
    
    # Print the table of characters and their codes
    print("Char | Huffman Code")
    print("-------------------")
    for char, code in codes.items():
        print(f"  {char}   |    {code}")

# Example usage

data = "hello"
huffman_encoding(data)

'''
Huffman Encoding is a popular algorithm used for lossless data compression. The algorithm follows a greedy strategy by
repeatedly merging the two least frequent nodes to create an optimal binary tree, known as the Huffman Tree.

A **greedy algorithm** is a problem-solving strategy that builds a solution piece by piece, always choosing the next 
step that offers the **most immediate benefit** or **optimal local choice**. It does this without worrying about how 
the choice will affect the overall solution.

### Key Characteristics of Greedy Algorithms:
1. **Local Optimization**: At each step, it makes the best choice available at that moment.
2. **Irrevocable Decisions**: Once a choice is made, it’s never reconsidered.
3. **Efficiency**: Greedy algorithms are often faster and simpler since they don't explore all possible solutions.

### Example:
In **Huffman Encoding**, a greedy approach is used by repeatedly combining the two nodes with the lowest frequency 
until only one node remains. This creates an optimal tree structure for data compression.
'''