
# For example 55 is Kaprekar numbers because:
# 55 = 30 + 25
# 55 ** 2 = 3025
# 45 is Kaprekar too:
# 45 = 20 + 25
# 45 ** 2 = 2025
# It is important to understand that these number can have even not equally long pairs. For example the number 2223 is Kaprekar:
# 2223 = 494 + 1729
# 2223 ** 2 = 4941729
# The task is to write a function is_kaprekar() that should return True or False showing whether the given int number is Kaprekar.


def is_kaprekar(num):
    
    string_num = str(num**2)
    for i in range(1,len(string_num)):
        if int(string_num[:i])+int(string_num[i:])==num:
            return True
    return False
    
# Small visual tests:    
kaprekars = [45, 55, 99, 297, 703, 999, 2223, 2728, 4879]
for x in kaprekars:
    print(f"{x}: should be True = {is_kaprekar(x)}")
    print(f"{x + 5}: should be False => {is_kaprekar(x + 5)}")