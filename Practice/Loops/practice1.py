# for loop practice

# Qs: Accept an integer n and Print Hello World n times.

n = int(input("Enter value of n: "))

for i in range(n):
    print("Hello World")

# Qs: Print natural number up to n

n = int(input("Enter n: "))

for i in range(1, n+1):
    print(i)

# Qs: Reverse for loop. Print n to 1

n = int(input("Enter n: "))

for i in range(n, 0, -1):
    print(i)

# Qs: Take a number as input and print its table

table_number = int(input("Enter number: "))

for count in range(1, 11):
    print(table_number * count)

# Qs: Sum up to n terms.

n = int(input("Enter n: "))
sum = 0

for i in range(n+1):
    sum += i
print(sum)