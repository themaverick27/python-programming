# while loop practice

# Qs: Separate each digit of a number and print it on the new line.

n = int(input("Enter number: "))

while n > 0:
    digit = n%10
    n //= 10
    print(digit)

# Qs: Accept a number and print its reverse.

num = int(input("Enter number: "))

reverse_num = 0
while num != 0:
    digit = num%10
    reverse_num = (reverse_num * 10) + digit
    num //= 10

print(reverse_num)


# Qs: Accept a number and check if it is a palindromic number.

num = int(input("Enter number: "))

org_num = num # save original number for later check (palindromic check)

reverse_num = 0
while num != 0:
    digit = num%10
    reverse_num = (reverse_num * 10) + digit
    num //= 10

if org_num == reverse_num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")