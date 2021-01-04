tests = [
    (3, [1, 2, 3, 1, 2, 4], [3, 2, 4]),
    (2, [5, 4, 1, 3], [5, 4]),
    (4, [1, 2, 1], [])

]


def remove_smallest(num, list_):
    new_list = list_.copy()
    if num <= len(list_):
        for _ in range(num):
            new_list.remove(min(new_list))
    else:
        new_list.clear()
    return new_list


print(remove_smallest(1, tests))
for test in tests:
    number, original, expected = test
    actual = remove_smallest(number, original)
    assert actual == expected, "Wrong :("
    assert actual is not original, "You can't change original list"
