def insertion_sort(arr):
    n = len(arr)  

    # Start from the second element (index 1) to the end of the array
    for i in range(1, n):
        # Traverse the sorted portion of the array backwards
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                # If the current element is smaller, swap them
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    
    return arr  

