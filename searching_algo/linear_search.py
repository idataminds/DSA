def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
arr = [10, 15, 30, 70, 80, 60, 20, 90, 40]
target = 20
result = linear_search(arr, target)
print(result)  # Output: 6

