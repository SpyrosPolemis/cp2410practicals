def find_smallest(data_list):
    """
    Find the smallest element in a list
    :param data_list: a list of elements
    :return: smallest element
    """
    if not data_list:  # Check for empty list
        return None
    smallest = data_list[0]
    for i in data_list:
        if i < smallest:
            smallest = i
    return smallest
    # Algorithm runs in O(n)
