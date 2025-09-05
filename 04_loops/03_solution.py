# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

n = int(input("enter number n: "))

for num in range(1, 11):
    if num == 5:
        continue
    
    print(n * num)