# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar.


# def is_palindrome(s):
#     s2=s.replace(",","").replace(" ","").replace("!","").replace("?","").lower()
#     return s2==s2[::-1]
    

# def is_palindrome(n):
#     n = n.lower()
#     n = ''.join(char for char in n if char.isalpha())
#     return n==n[::-1]


def is_palindrome(s):
    symbols = [",","!"," "]
    for symbol in symbols:
        s=s.replace(symbol,"").lower()      
    return s==s[::-1]
        
    

print(is_palindrome("racecar")) # True
print(is_palindrome("Race Car")) # True
print(is_palindrome("A man, a plan, a canal, Panama!"))  # True

