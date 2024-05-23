WORDS = ["I", "really", "like", "legumes", "such", "as", "beans", "and", "peas", "mmm", "beans"]


def count_occurrences(word_list, target_word):
    """
    Count the number of times a word appears in a list
    :param word_list:
    :param target_word:
    :return:
    """
    occurrences = 0
    for word in word_list:
        if word == target_word:
            occurrences += 1
    return occurrences


print(count_occurrences(WORDS, "legumes"))  # Should be 1
print(count_occurrences(WORDS, "beans"))  # Should be 2
print(count_occurrences(WORDS, "existential"))  # Should be 0
