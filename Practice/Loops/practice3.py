# for loop practice

# Qs: Reverse a string without using in-build functions.

s = input("Enter word: ")

length = len(s)
reverse_s = ""
for i in range(length-1, -1, -1):
    reverse_s += s[i]

print(reverse_s)


# Qs: Check string is Palindrome or not.

if s == reverse_s:
    print("Palindrome String")
else:
    print("Not a Palindrome String")

# Qs: Count all letters, digits, and special symbols from a given string. 
# Given: str1 = "P@#yn26at^&i5ve", Expected o/p: Chars = 8, Digits = 3, Symbol = 4

word = input("Enter word: ")

char_count = 0
digit_count = 0
symbol_count = 0
for ch in word:
    if ch >= '0' and ch <= '9':
        digit_count += 1
    elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
        char_count += 1
    else:
        symbol_count += 1

print(f"Number of characters is {char_count}, digits is {digit_count} and symbol is {symbol_count} in {word}")