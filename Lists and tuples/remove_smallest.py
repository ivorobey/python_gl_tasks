# Remove one - smallest - item from given list.


tests = [([1, 2, 3, 4, 5], [2, 3, 4, 5]),
         ([5, 4, 1, 3], [5, 4, 3]), ([1, 2, 1], [2, 1])]


def remove_smallest(list_):
    list2 = list()
    list_.remove(min(list_))

    for item in list_:
        list2.append(item)
    return list2


print(remove_smallest(tests))
for test in tests:
    result = remove_smallest(test[0])
    assert result == test[1], "Wrong :("
    assert result is not test[0], "You can't change original list"
