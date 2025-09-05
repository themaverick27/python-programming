# Problem: Check if a number is prime.

n = int(input("enter a number n: "))

if n <= 1:
    print("not prime!")
    exit()
else:
    for num in range(3, n):
        if n % num == 0:
            print("Not a prime number")
            exit()

print("prime number")