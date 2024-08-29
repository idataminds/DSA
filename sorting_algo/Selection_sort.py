def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the first unsorted element is the minimum
        min_index = i
        # Find the index of the minimum element in the remaining unsorted array
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr
