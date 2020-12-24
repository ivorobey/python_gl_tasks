# https://stackoverflow.com/questions/44425733/equilibrium-index-in-python-2-7
def get_equilibriums(list_):
    A = list_

    if len(A) == 0:
        return "Empty list, no integers to work with"
    else:
        equi = []
        x = 0
        
        for i in A:
            leftList = A[0:x]
            rightList = A[x+1:]
            if sum(leftList) == sum(rightList):
                equi.append(x)
            x += 1

        if len(equi) == 0:
            return -1
        else:
            return equi

print(get_equilibriums([-1, 3, -4, 5, 1, -6, 2, 1]))
print(get_equilibriums([1, 3, 100, 2, 2]))