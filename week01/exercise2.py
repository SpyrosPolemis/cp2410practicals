from random import randint


def find_max(numbers):
    """Return max number in a list of numbers. O(n)"""
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


print(find_max([]))  # 0
print(find_max([2, 3, 5, 7, 11]))  # 11
print(find_max([5, 5, 5, 5, 5, 10]))  # 10
print(find_max([randint(0, 100) for i in range(10000)]))  #
