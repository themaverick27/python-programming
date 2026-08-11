# for loop practice

# Qs: Factorial of a number

num = int(input("Enter number: "))
fact = 1

if num == 0 or num == 1:
    print(fact)
else:
    for i in range(num, 1, -1):
        fact *= i

print(fact)


# Qs: Print the sum of all even & odd numbers in a range separately.

start = int(input("Enter starting value of range: "))
end   = int(input("Enter ending value of range: "))

even_sum = 0
odd_sum = 0

for i in range(start, end+1):
    if i%2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"Even sum: {even_sum} and Odd sum: {odd_sum} between range {start} and {end}.")

# Qs: Print all the factors of a number.

num = int(input("Enter number: "))

for i in range(1, num+1):
    if num%i == 0:
        print(i)

# Qs: Accept a number and check if it a perfect number or not. 
# A number whose sum of factors is equal to the number itself. Ex: 6 = 1, 2, 3

num = int(input("Enter number: "))

sum_factor = 0
for i in range(1, num+1):
    if num%i == 0:
        sum_factor += i

if (sum_factor - num) == num:
    print("Perfect number")
else:
    print("Not a Perfect number")


# Qs: Check wether the number is prime or not.

num = int(input("Enter number: "))

if num <= 1:
    print("Not prime")

for i in range(2, num):
    if num%i == 0:
        print("Not a Prime Number")
        break

else:
    print("Prime number")