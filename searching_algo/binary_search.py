def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == target:
            return middle  # Return the index where the target is found
        elif arr[middle] < target:
            low = middle + 1  # Update low to search in the right half
        else:
            high = middle - 1  # Update high to search in the left half
    return -1  # Return -1 if the target is not found

# Example usage:
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 20
result = binary_search(arr, target)
print(result)  # Output: 1
Explanation:
