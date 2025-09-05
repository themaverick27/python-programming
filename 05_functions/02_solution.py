# Problem: Create a function that takes two numbers as parameters and returns their sum.

def add(num1, num2): # parameters
    return num1 + num2

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

ans = add(num1, num2) # arguments
print(ans)