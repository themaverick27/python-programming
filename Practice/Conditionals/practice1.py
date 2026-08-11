# Q1. Accept two numbers and print the greatest between them.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number2 > number1: 
    print(f"{number2} is greater than {number1}")
else:
    print("Both numbers are equal")

# Q2. Accept the gender from the user as char and print the respective greeting message. Ex - Good Morning Sir (on the basis of gender)

gender = input("Enter your gender (as 'M' for Male or 'F' for Female): ")

if gender == 'M':
    print("Good Morning Sir")
else:
    print("Good Morning Maam")

# Q3. Accept an integer and check whether it is an even number or odd.

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even Number")
else: 
    print("Odd Number")

# Q4. Accept name and age from the user. Check if the user is a valid voter or not. Ex- “hello shery you are a valid voter”

name = input("Enter you name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you are a valid voter!")
else:
    print(f"Hello {name}, you are not a valid voter!")

# Q5. Accept a year and check if it a leap year or not.

year = int(input("Enter an year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year!")

else:
    print(f"{year} is not a leap year!")

# 