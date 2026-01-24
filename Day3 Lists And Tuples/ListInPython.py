    # Create a list of numbers
num = [10, 20, 30, 40, 50]
# List Methods Examples

# append() - Add an item to the end of the list
num.append(60)
print("After append(60):", num)

# extend() - Add multiple items to the end of the list
num.extend([70, 80])
print("After extend([70, 80]):", num)

# insert() - Insert an item at a specific position
num.insert(2, 25)
print("After insert(2, 25):", num)

# remove() - Remove the first item with the specified value
num.remove(25)
print("After remove(25):", num)

# pop() - Remove and return item at given index (default: last item)
popped = num.pop()
print("After pop():", num, "Popped value:", popped)

# index() - Return index of first item with specified value
idx = num.index(30)
print("Index of 30:", idx)

# count() - Return number of items with specified value
count = num.count(20)
print("Count of 20:", count)

# sort() - Sort the list in ascending order
num.sort()
print("After sort():", num)

# reverse() - Reverse the list
num.reverse()
print("After reverse():", num)

# copy() - Return a shallow copy of the list
num_copy = num.copy()
print("Copy of list:", num_copy)

# clear() - Remove all items from the list
# num.clear()

# List Slicing Examples
print("\n--- Slicing Examples ---")
print("num[1:4]:", num[1:4])  # Elements from index 1 to 3
print("num[:3]:", num[:3])    # Elements from start to index 2
print("num[2:]:", num[2:])    # Elements from index 2 to end
print("num[::2]:", num[::2])  # Every 2nd element
print("num[::-1]:", num[::-1]) # Reversed list

    