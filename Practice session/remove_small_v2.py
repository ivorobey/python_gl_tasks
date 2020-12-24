tests = [
    (3, [1, 2, 3, 1, 2, 4], [3, 2, 4]),
    (2, [5, 4, 1, 3], [5, 4]),
    (4, [1, 2, 1], [])

]
# for elem in tests:
#     for tuples in elem:
#         print(type(tuples))

def remove_smallest(num, list_):
    new_list = []
    for listi in list_:
        for elem in listi[1::2]:
            new_list.append(elem)
    print("NEW list: ",new_list)
    
#     print(sorted(new_list[1].))
#     # for elem in new_list[1]:
    list2=[]
    for i in new_list:
        if type(i)==list:
            remove_smallest(i)
        else:
            list2.append(i)
    return min(list2)
        
  

    


print(remove_smallest(1, tests))
# for test in tests:
#     number, original, expected = test
#     actual = remove_smallest(number, original)
#     assert actual == expected, "Wrong :("
#     assert actual is not original, "You can't change original list"
