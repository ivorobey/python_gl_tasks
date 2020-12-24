# The task is to write a function which should generate a list with integers that in sum will give zero.

def gen_list(num):
    spisok = list()
    for i in range(1, num):
        spisok.append(i)
    last_elem = -sum(spisok)
    spisok.append(last_elem)
    return spisok


print(gen_list(5))
