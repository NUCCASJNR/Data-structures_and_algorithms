## Search Algorithms

## Resources
[Search algorithm](https://en.wikipedia.org/wiki/Search_algorithm)

[Space complexity (1)](https://www.geeksforgeeks.org/g-fact-86/)

## search algorithm and how can it be implemented in python

-A search algorithm is a method for finding a specific item or set of items within a data structure, such as an array, list, or tree. There are many types of search algorithms, including linear search, binary search, depth-first search, and breadth-first search. Each algorithm has its own strengths and weaknesses and is suitable for different types of data.

- In Python, search algorithms can be implemented using functions. Here is an example of a linear search algorithm implemented in Python:

```bash
def linear_search(lst, item):
    """
    Performs a linear search to find the index of an item in a list.
    Returns -1 if the item is not found.
    """
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1
```

- This function takes two arguments: a list lst to search through and an item to find. It then iterates through the list using a for loop, comparing each element to the item we are searching for. If the item is found, the function returns its index. If the item is not found, the function returns -1.

Here is an example of how to use the linear_search function:

```bash
my_list = [1, 2, 3, 4, 5]
item_to_find = 3
result = linear_search(my_list, item_to_find)
print(result)  # Output: 2
```
