# Let's count animals on a farm!
# The farm contains rabbits and chickens. We know counts of heads and legs and need to get the number of rabbits (they have 1 head and 4 legs each!) and 
# the number of chickens (1 head + 2 legs).
# For example, we have 3 heads and 10 legs. By brute-force, we should get 2 rabbits and 1 chicken.
# The function should receive heads and legs and return numbers for rabbits and chickens or return the string "Not possible".

def count_rabbits_chickens(heads, legs):
    if legs % 2 !=0 or heads ==0 or heads > legs:
        return 'not possible'
    else:  
        r = int((legs + (-2*heads))/2)
        c = int(heads - r)
        return r,c
    
    
print(count_rabbits_chickens(3, 10))  # 2, 1