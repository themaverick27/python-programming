num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# if user inputs num2 as 0, then ZeroDivisionError: division by zero <- so, this is an exception

try:
    result = num1 / num2
    print(f"Division of {num1}/{num2} is: {result}")
except ZeroDivisionError:
    print("You cannot divide number by 0.")
except Exception as e:
    print(f"Error occurred: {e}")
else:
    print("No exception occurred!")
finally:
    print("Run always, no matter what")

print("Done")


