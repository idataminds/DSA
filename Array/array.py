# Creating an array (list) in Python
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Accessing elements
print("First element:", arr[0])  # Output: First element: 10
print("Last element:", arr[-1])  # Output: Last element: 90

# Modifying elements
arr[2] = 35  # Change the third element (index 2) to 35
print("Modified array:", arr)  # Output: Modified array: [10, 20, 35, 40, 50, 60, 70, 80, 90]

# Adding elements
arr.append(100)  # Add 100 to the end of the array
print("Array after appending:", arr)  # Output: Array after appending: [10, 20, 35, 40, 50, 60, 70, 80, 90, 100]

# Inserting elements
arr.insert(1, 15)  # Insert 15 at index 1
print("Array after inserting:", arr)  # Output: Array after inserting: [10, 15, 20, 35, 40, 50, 60, 70, 80, 90, 100]

# Removing elements
arr.remove(50)  # Remove the first occurrence of 50
print("Array after removing 50:", arr)  # Output: Array after removing 50: [10, 15, 20, 35, 40, 60, 70, 80, 90, 100]

# Popping elements
popped_element = arr.pop()  # Remove and return the last element
print("Popped element:", popped_element)  # Output: Popped element: 100
print("Array after popping:", arr)  # Output: Array after popping: [10, 15, 20, 35, 40, 60, 70, 80, 90]

# Finding the index of an element
index_of_40 = arr.index(40)  # Find the index of the first occurrence of 40
print("Index of 40:", index_of_40)  # Output: Index of 40: 4

# Checking if an element exists
if 70 in arr:
    print("70 is in the array")  # Output: 70 is in the array

# Length of the array
print("Length of the array:", len(arr))  # Output: Length of the array: 9

# Iterating through the array
print("Iterating through the array:")
# Output:
# Iterating through the array:
# 10
# 15
# 20
# 35
# 40
# 60
# 70
# 80
# 90
for item in arr:
    print(item)

# Slicing the array
print("Sliced array (first three elements):", arr[:3])  # Output: Sliced array (first three elements): [10, 15, 20]

