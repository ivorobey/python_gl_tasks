
def draw_table():

    # for i in range(1, 11):
    #     for j in range(1, 11):
    #         print('{:>4}'.format(str(i*j)), end='')
    #     print('\t')

    multiples = [n for n in range(1, 15) for j in range(1, 15)]
    return str(multiples)

print(draw_table())
