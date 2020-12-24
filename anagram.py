# An anagram is the result of rearranging the letters of a word to produce a new word. Anagrams are case insensitive
# Examples:
# • foefet is an anagram of toffee
# • Buckethead is an anagram of DeathCubeK


# Task:
# write a program which return True/False based on are two passed string args are anagrams or not.

def is_anagram(str1, str2):
    str1="".join(sorted(list(str1.lower())))
    str2="".join(sorted(list(str2.lower())))
    return str1 == str2
    

    
print(is_anagram("AbbA", "BBaA")) # True