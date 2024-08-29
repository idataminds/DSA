def quick_sort(arr):
    if len(arr)<=1:
        return arr
    Pivot = arr[-1]
    Left = [x for x in arr if x[:-1] <= Pivot]
    Right = [x for x in arr if x[:-1] > Pivot]

    Left = quick_sort(Left)
    Right = quick_sort(Right)

    return (Left + [Pivot] + Right)
