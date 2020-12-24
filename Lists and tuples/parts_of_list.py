# Write a function that gives all the ways to divide a list of at least two elements in two non-empty parts.

# Each two non empty parts will be in a tuple
# Each part will be in a string
# Elements of a pair must be in the same order as in the original array.
# Example:
# >>> a = ["az", "toto", "picaro", "zone", "kiwi"]
# >>> partlist(a)
# [('az', 'toto picaro zone kiwi'), ('az toto', 'picaro zone kiwi'), ('az toto picaro', 'zone kiwi'), ('az toto picaro zone', 'kiwi')]


test_data = ["az", "toto", "picaro", "zone", "kiwi"]


def partlist(list_):
    tmp_list = list()
    res_list = list()
	
    index = 1

    while index < len(list_):
        tmp_list.append(" ".join(list_[:index]))
        tmp_list.append(" ".join(list_[index:]))
        index += 1
# iter() is an iterator over a sequence. [x] * n produces a list containing n quantity of x, i.e. a list of length n, where each element is x. 
# *arg unpacks a sequence into arguments for a function call. 
# Therefore you're passing the same iterator 3 times to zip(), and it pulls an item from the iterator each time.
    for i in zip(* [iter(tmp_list)] * 2):
        res_list.append(i)

    return res_list


print(partlist(test_data))

