"""
This module demonstrates the usage of Python dictionaries, including basic operations such as 
creating, updating, accessing, and manipulating dictionary data structures.

A dictionary in Python is an unordered collection of items. Each item is stored as a key-value pair, 
where each key is unique. Dictionaries are mutable, meaning they can be changed after their creation.

Key Features:
- Keys must be immutable types (e.g., strings, numbers, tuples).
- Values can be of any data type and can be duplicated.
- Dictionaries are defined using curly braces `{}`.

Example Usage:
1. Creating a dictionary:
    dict_example = {
         "key": "value",
         "name": "praveen",
         "cgpa": 7.7,
         "age": 23,
         "is_adult": True
    }

2. Accessing values:
    print(dict_example["name"])  # Output: praveen

3. Updating values:
    dict_example["name"] = "Praveen Bhardwaj"  # Updates the name
    dict_example["phone_number"] = "1234567890"  # Adds a new key-value pair

4. Nested dictionaries:
    info = {
         "name": "Praveen",
         "subjects": {
              "py": 22,
              "ml": 33,
              "da": 23,
         }
    }
    print(info["subjects"])  # Accessing nested dictionary

5. Using methods:
    print(info.get("name"))  # Safely access value using get method
    print(info.get("name1"))  # Returns None if key not found

6. Updating dictionaries:
    new_dict = {"city": "bangalore"}
    info.update(new_dict)  # Merges new_dict into info

This module serves as a comprehensive guide to understanding and utilizing dictionaries in Python.
"""

# Example dictionary
dict_example = {
    "key": "value",
    "name": "praveen",
    "cgpa": 7.7,
    "age": 23,
    "is_adult": True
}

# Accessing a value
print(dict_example["name"])  # Output: praveen

# Updating a value
dict_example["name"] = "Praveen Bhardwaj"  # Updates the name
dict_example["phone_number"] = "1234567890"  # Adds a new key-value pair
print(dict_example)

# Nested dictionary
info = {
    "name": "Praveen",
    "subjects": {
        "py": 22,
        "ml": 33,
        "da": 23,
    }
}
print(info["subjects"])  # Accessing nested dictionary

# Using methods
print(info.get("name"))  # Accessing value using get method
print(info.get("name1"))  # Returns None if key not found

# Updating dictionary
new_dict = {"city": "bangalore"}
info.update(new_dict)  # Merges new_dict into info
print(info)