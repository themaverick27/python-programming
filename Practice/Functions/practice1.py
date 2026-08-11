# Qs: Take a string input from user. Check for Palindrom or not. (Use Function)

def checkPalindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


s = input("Enter string: ")

if(checkPalindrome(s)):
    print(f"{s} is a Palindrome string")
else:
    print(f"{s} is not a Palindrome string")