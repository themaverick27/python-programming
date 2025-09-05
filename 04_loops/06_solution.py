# Problem: Compute the factorial of a number using a while loop.

n = int(input("enter number n: "))

if n < 0:
    print("enter valid number!")
    exit()

fact = 1
while n >= 1:
    fact = fact * n
    n -= 1

print(fact)