#!/usr/bin/python3
"""
This module implements the linear search algorithm
Linear search algorithm also known as seqential search algorithm
is a type of searching algoritm that compares each every element
in a list till it finds the desired element
"""


def linear_search(li, search_value):
    for i in range(len(li)):
        if li[i] == search_value:
            return i
    return None
