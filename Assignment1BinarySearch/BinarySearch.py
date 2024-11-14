def binary_search(arr, low, high, key):
    # Base condition
    if high >= low:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # If the element is present at the middle itself
        if arr[mid] == key:
            return mid
        
        # If the element is smaller than mid, it must be in the left subarray
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        
        # If the element is larger than mid, it must be in the right subarray
        else:
            return binary_search(arr, mid + 1, high, key)
    
    # Element is not present in the array
    else:
        return -1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

    
# Example usage
arr = [2, 3, 4, 10, 40]
key = 10

# Run binary search on the array
result = binary_search(arr, 0, len(arr) - 1, key)

# Print result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in array")


'''
The Binary Search algorithm works by dividing the search interval in half repeatedly. If the value of the search key
is less than the item in the middle, it narrows the interval to the lower half. Otherwise, it narrows it to the upper
half.
### Time Complexity Analysis

1. **Best Case**: (O(1))
   - When the element is found at the middle index in the first step itself.

2. **Average and Worst Case**: ( O(log n))
   - In each step, the Binary Search algorithm divides the search space by half. 
   Therefore, the time complexity for (n) elements is (O(log n)).
   - This logarithmic time complexity is due to the divide-and-conquer approach, which reduces the problem size by
    half in each recursive call.

**Space Complexity**: (O(log n)) for the recursive version because each recursive call consumes space in the 
function call stack.
'''