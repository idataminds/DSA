import heapq

heap = []  # Create an empty heap

# Push elements into the heap
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

# Pop the smallest element
smallest = heapq.heappop(heap)
print(smallest)  # Output: 1

# Convert a list into a heap
nums = [4, 2, 9, 7]
heapq.heapify(nums)
print(nums)  # Output: [2, 4, 9, 7] (min-heap)
