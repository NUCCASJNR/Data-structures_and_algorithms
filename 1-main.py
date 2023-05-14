#!/usr/bin/python3

binary_search = __import__('1-binary').binary_search

array = sorted([10, 1, 42, 3, 23, 4, 42, 6, 7, -1, 9])
search = [23, 100,  10, -1, 9, 7, 6, 42]
for value in search:
    index = binary_search(array, value)
    if index != -1:
        print(f"Found {value} at index: {index}")
    else:
        print(f"{value} not found in the array")
