from random import randint


def find_max(numbers):
    """Return max number in a list of whole numbers. O(n)"""
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


def find_min(numbers):
    """Return min number in a list of whole numbers. O(n)"""
    min_number = 100
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number


print(find_max([]))  # 0
print(find_max([2, 3, 5, 7, 11]))  # 11
print(find_max([5, 5, 5, 5, 5, 10]))  # 10
print(find_max([randint(0, 100) for i in range(10000)]))  # most likely 100

print(find_min([]))  # 100
print(find_min([2, 3, 5, 7, 11]))  # 2
print(find_min([5, 5, 5, 5, 5, 10]))  # 5
print(find_min([randint(0, 100) for j in range(10000)]))  # most likely 0
