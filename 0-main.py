#!/usr/bin/python3

linear_search = __import__('0-linear').linear_search

array = [10, 1, 42, 3, 4, 42, 6, 7, -1, 9]
search = [23, 10, -1, 9, 7, 6, 42]
for value in search:
    index = linear_search(array, value)
    if index:
        print(f"Found {value} at index: {index}")
    else:
        print(f"{value} not found in the array")
