from task2 import find_smallest_index


def selection_sort(data_list):
    """
    Sort a list using selection sort. Time complexity: _______
    :param data_list: a list of elements
    :return: sorted list
    """
    if not data_list:
        return None
    sorted_list = []
    for i in range(len(data_list)):
        smallest_index = find_smallest_index(data_list)
        sorted_list.append(data_list.pop(smallest_index))
    return sorted_list
    # O(n^2) since it has to go through list twice for each element
    # for list size, find smallest (go through list n times)


print(selection_sort([5, 3, 2, 1, 6]))
