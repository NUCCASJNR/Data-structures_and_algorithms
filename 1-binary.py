#!/usr/bin/python3
"""
This module implements the binary search algorithm in python
Binary search is more faster than linear search in terms of big arrays
"""

def binary_search(li, element):
    low = 0
    high= len(li) - 1

    while low <= high:
        mid = (high + low) // 2
        if li[mid] == element:
            return mid
        elif li[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1
