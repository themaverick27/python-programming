# Problem: Given a string s, find the first non-repeated character.

s = input("enter string s: ")

for char in s:
    if s.count(char) == 1:
        print(char)
        break