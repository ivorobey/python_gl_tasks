#https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/

string_ = "Revert me please:)"

def method_1(string_):#simple
    return string_[::-1]
    
def method_2(string_):# .join() method merges all of the characters resulting from the reversed iteration into a new string
    reversedstring=''.join(reversed(string_)) 
    return(reversedstring) 
    
def method_3(string_):#recursion
    s=string_
    if len(s) == 0: 
        return s 
    else: 
        return method_3(s[1:]) + s[0] 


def method_4(string_):
    s1 = ''
    for c in string_:
        s1 = c + s1  # appending chars in reverse order
    return s1
    
print("1 -->", method_1(string_))
print("2 -->", method_2(string_))
print("3 -->", method_3(string_))
print("4 -->", method_4(string_))



