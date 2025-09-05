# Problem: Reverse a string using a loop.

s = input("enter string s: ")

# reverse_s = s[::-1]
# print(reverse_s)

reverse_s = ""
for ch in s:
    reverse_s = ch + reverse_s

print(reverse_s)