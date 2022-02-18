"""
Michael Balestriere
Week 3 - count the characters
"""
# This part of my code sets each variable equal to 0
vowel_count = 0
space_count = 0
lower_count = 0
upper_count = 0
punctuation_count = 0
digit_count = 0

userString = input("enter any string!  ")

# For each character in the userString, the loop checks to see if it is equal to any of the letters, numbers, or punctuation
for c in userString:
    if c in "AEIOUaeiou":
        vowel_count += 1
    if c in " ":
        space_count += 1
    if "a" <= c <= "z":
        lower_count += 1
    if "A" <= c <= "Z":
        upper_count += 1
    if c in "0123456789":
        digit_count += 1
    if c in "~`@#$%^&*()_-+=/[]{}\|':;,.<>?!":
        punctuation_count += 1

# This part of my code prints out how many characters it found for each variable
print("upper case count = ", upper_count)
print("lower case count = ", lower_count)
print("space count = ", space_count)
print("vowel count = ", vowel_count)
print("digits count = ", digit_count)
print("punctuation count = ", punctuation_count)
