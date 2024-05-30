def binary_search(data_list, target):
    low = 0
    high = len(data_list)
    while low <= high:
        mid = (low + high) / 2
        if data_list[mid] < target:
            low = mid + 1
        elif data_list[mid] > target:
            high = mid - 1
        else:
            return mid
    return None

