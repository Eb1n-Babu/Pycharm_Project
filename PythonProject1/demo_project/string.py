# Reverse a string
text = "Python"
reversed_text = text[::-1]
print("Reversed String:", reversed_text)

# Count vowels in a string
vowels = "aeiouAEIOU"
sentence = "Hello World"
count = sum(1 for char in sentence if char in vowels)
print("Number of vowels:", count)

# Uppercase and lowercase conversion
original_text = "Learning Python"
print("Uppercase:", original_text.upper())
print("Lowercase:", original_text.lower())


"""reverse a string"""
str1 = "Hello World"
print(str1[::-1])
print(str1[::1])

for ch in str1:
    print(ch, end="  ")