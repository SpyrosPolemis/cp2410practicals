def find_smallest_index(data_list):
    """
    Find the smallest element in a list
    :param data_list: a list of elements
    :return: smallest element
    """
    if not data_list:  # Check for empty list
        return None
    smallest = data_list[0]
    for i, number in enumerate(data_list):
        if number < smallest:
            smallest = number
            index = i
    return index
    # Algorithm runs in O(n)


print(find_smallest_index([1, 2, -8, 0, 5, 6, 10, 0]))  # outputs: 2
print(find_smallest_index([1, 2, 3, 0, 4, 5, 6, 7, 8, 0, 9, 10]))  # outputs: 3
