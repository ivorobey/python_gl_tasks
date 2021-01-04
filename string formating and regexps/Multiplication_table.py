
def draw_table():

    for i in range(1, 5):
        for j in range(1, 5):
            print('{:>4}'.format(str(i*j)), end='')
        print('\t')


print(draw_table())
