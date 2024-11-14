'''
Problem Statement:
Develop a program to design a class for Concurrent Quick Sort Using
Divide and Conquer Strategies
'''
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # Choose the middle element as the pivot
    mid = (high + low) // 2
    pivot = arr[mid]

    # Move the pivot to the end for partitioning
    arr[mid], arr[high] = arr[high], arr[mid]
    
    print(f"Current pivot: {pivot}")

    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1 
    # Move the pivot to its correct position
    arr[i], arr[high] = arr[high], arr[i]

    print(f"Array: {arr}")
    print(f"Pivot position: {i}\n")

    return i

# Example usage
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array is:", arr)

'''
1. **Divide**: The array is divided into two parts based on a pivot element. Elements smaller than the pivot go to its left, 
and elements greater than the pivot go to its right. This partitioning separates the array into smaller sub-arrays.

2. **Conquer**: Quick Sort is recursively applied to each of these sub-arrays. Each recursive call further divides the array 
until each sub-array has only one element, which is inherently sorted.

3. **Combine**: Quick Sort combines results by leveraging the pivot’s position, but it doesn’t explicitly merge arrays like 
Merge Sort. Instead, the placement of elements around the pivot naturally leads to a sorted array.

Thus, Quick Sort is a classic example of the divide and conquer technique.
'''