"""
Set Operations and Methods Demonstration

This module demonstrates various set operations and methods in Python:

- Set Definition: Creates a set with duplicate elements (duplicates are automatically removed)
- Empty Set: Shows how to create an empty set using set()
- Set Methods:
    - add(): Adds a single element to the set
    - remove(): Removes a specified element; raises error if element not found
    - discard(): Removes a specified element; does not raise error if element not found
    - pop(): Removes and returns an arbitrary element from the set
    - clear(): Removes all elements from the set
    - union(): Returns a new set containing all elements from both sets
    - intersection(): Returns a new set containing only common elements between two sets

Sets are unordered collections of unique elements enclosed in curly braces {}.
"""

# Set Definition
my_set = {1, 2, 3, 4, 5, 5, 5, 5}  # Duplicates are removed
print("Initial Set:", my_set)  # Output: {1, 2, 3, 4, 5}
print("Type of my_set:", type(my_set))  # Output: <class 'set'>

# Empty Set
empty_set = set()
print("Empty Set:", empty_set)  # Output: set()

# Set Methods Demonstration
my_set.add(6)  # Adding element to set
print("After adding 6:", my_set)  # Output: {1, 2, 3, 4, 5, 6}
print("After removing 3:", my_set)  # Output: {1, 2, 4, 5, 6}
print("Element not found for removal.")

my_set.discard(10)  # Removing element from set, does not throw error if element not found
print("After discarding 10 (not found):", my_set)  # Output: {1, 2, 4, 5, 6}

removed_element = my_set.pop()  # Removes and returns an arbitrary element from the set
print("Removed Element:", removed_element)
print("Set after pop:", my_set)

my_set.clear()  # Clears the set
print("Set after clear:", my_set)  # Output: set()

# Union and Intersection
my_set2 = {1, 2, 3, 4, 5, 6, 7, 8}
union_set = my_set2.union(my_set)  # Returns a new set with elements from both sets
print("Union of my_set2 and my_set:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

intersection_set = my_set.intersection(my_set2)  # Returns a new set with elements common to both sets
print("Intersection of my_set and my_set2:", intersection_set)  # Output: set()