# Problem: Write a function to calculate and return the square of a number.

def square(num):
    return num ** 2

input_n = int(input("enter number n: "))
result = square(input_n)
print(result)