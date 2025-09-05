# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("enter number n: "))

sum = 0
for num in range(1, n+1):
    if num % 2 == 0:
        sum += num

print(sum)