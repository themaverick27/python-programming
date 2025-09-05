# Problem: Create a recursive function to calculate the factorial of a number.

def factorial(num):
    if num == 1 or num == 0:
        return 1
    

    return num * factorial(num - 1)

input_n = int(input("enter number n: "))
result = factorial(input_n)
print(result)