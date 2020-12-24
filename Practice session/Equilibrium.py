# Equilibrium index of a list is such index that divides the list in two parts with the same total sum.

# Here the list is A of length N and Equilibrium index is E:

# A[0] + A[1] + ... + A[E−1] == A[E+1] + ... + A[N−2] + A[N−1].
# In other words: the SUM of everything PRIOR to E equals to the SUM of items AFTER.

# Simple example - we have a list: a = [3, 1, 3, 2, 2]. Equilibrium index here is 2 because a[0] + a[1] == a[3] + a[4] (3 + 1 == 2 + 2).




def get_equilibriums(list_):
    A=list_
    if len(A) == 0: #If we're working with an empty list, the method should give us an empty list message and terminate there
        return "Empty list, no integers to work with"
    else:
        equi = []
        x = 0
        length = len(A)
        rightSum = []
        leftSum = []
        # while x < length: (removed)
        # When we do for i in A, we're already iterating over each element i of the list A.
        # As such, there's no need for the while loop.
        for i in A:
            # You switched right and left sum; elements at the 'left' are at the beginning of the list
            # I also switched the name of the lists to leftList and rightList, to be more descriptive
            # (a list and a sum are different things)
            # I switched the i that was in the indexes to x. i is the integer on the list we're iterating over;
            # its position on the list, on the other hand, is being counted with x.
            leftList = A[0:x]  # Go from 0, since you want to count the first element.
            # We could also ommit the first index and it would begin from the first element
            rightList = A[x+1:]  # If we ommit the second index, it'll go until the last element
            if sum(leftList) == sum(rightList):
                # I changed equi.append(i) to equi.append(x), because i is the value we're iterating over, while
                # x is the counter (index) of the number being currently evaluated
                equi.append(x)
                # return equi (removed)
                # We don't want to return here. When we call return, the function exits!

            # What this would do is exit the function if the sum of the left list wasn't equal to the sum of the right.
            # This isn't what we want, so we'll just remove this
            # else: (removed)
            #     return -1 (removed)
            x += 1

        # No pass needed; that's another thing entirely, just a nil instruction

        # Now the loop is done, we have appended to equi all the equilibrium values.
        # It's time to exit the function by returning the list of equi values.
        # Since we must return -1 if no equilibrium indices exist, then we have to check for that as well
        if len(equi) == 0:
            return -1
        else:
            return equi
    

print(get_equilibriums([-1, 3, -4, 5, 1, -6, 2, 1]))
print(get_equilibriums([1, 3, 100, 2, 2]))