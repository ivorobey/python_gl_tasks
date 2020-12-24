# Task is to process all words from input sequence and return a list with lists from those words that are anagrams with others in their list

# list_ = ["tsar", "rat", "tar", "star", "tars", "cheese"]
# group_anagrams(list_)  # [["tsar", "star", "tars"], ["rat", "tar"], ["cheese"]]


# https://pythonworld.ru/moduli/modul-collections.html
from collections import defaultdict

test_list = ["tsar", "rat", "tar", "star", "tars", "cheese"]


def group_anagrams(test_list):

    dictionary = defaultdict(list)
    for word in test_list:
        dictionary[str(sorted(word.lower()))].append(word)
    return list(dictionary.values())
    


print(group_anagrams(test_list))
