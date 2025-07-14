from sqlalchemy.sql.base import elements


def reverse(str1):
    r_str1 = str1[::-1]
    return r_str1

print(reverse("hello"))

def palindrome(str1):
    p_str1 = str1[::-1]
    if p_str1 == str1:
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome("hello")

def count_vowels(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for elements in str1:
        if elements in vowels:
            print(vowels.index(elements))
        else:
            print("Not vowel")

count_vowels("hello")