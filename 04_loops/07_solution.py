# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    input_n = int(input("enter some input: "))
    
    if input_n >= 1 and input_n <= 10:
        break
    
    print(input_n)

print("Iteration completed! You entered number between 1 and 10.")