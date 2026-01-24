# TUPLES - Immutable sequences of elements
# Created with parentheses () or comma-separated values

# Creating tuples
my_tuple = (1, 2, 3, 4, 5)
another_tuple = ("apple", "banana", "cherry")
single_tuple = (42,)  # Comma required for single element
mixed_tuple = (1, "hello", 3.14, True)

print(my_tuple)
print(another_tuple)

# IMPORTANT TUPLE METHODS
print("\n--- Tuple Methods ---")

# 1. count() - Count occurrences of an element
fruits = ("apple", "banana", "apple", "cherry")
print(fruits.count("apple"))  # Output: 2

# 2. index() - Find position of first occurrence
print(fruits.index("banana"))  # Output: 1

# TUPLE SLICING - Extract portion using [start:end:step]
print("\n--- Tuple Slicing ---")

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(numbers[2:5])        # Output: (2, 3, 4) - start at index 2, end before 5
print(numbers[:4])         # Output: (0, 1, 2, 3) - from beginning to index 4
print(numbers[5:])         # Output: (5, 6, 7, 8, 9) - from index 5 to end
print(numbers[::2])        # Output: (0, 2, 4, 6, 8) - every 2nd element
print(numbers[::-1])       # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0) - reversed
print(numbers[1:7:2])      # Output: (1, 3, 5) - start 1, end 7, step 2

# Accessing elements
print(numbers[0])          # Output: 0 - first element
print(numbers[-1])         # Output: 9 - last element