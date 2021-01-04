# A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits.
# Нарциссическое число - это число, которое представляет собой сумму собственных цифр, каждая из которых возведена в степень числа цифр.
# For example, take 153 (3 digits):
#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

def narcissistic(test_number):
    num=test_number
    return num == sum([int(x) ** len(str(num)) for x in str(num)])
    
    
print(narcissistic(7))  # True
print(narcissistic(371)) # True
print(narcissistic(122)) # False
print(narcissistic(4887)) # False