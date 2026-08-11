# Qs: Create a random number guessing game with python.

target_number = 785
print("Rules of Games: ")
print("1. We have a target number which you have to guess.")
print("2. The target number lies in 1 to infnite.")
print("3. You have a total 10 chances to guess the target number.")
print("4. Press 0 to quit the game.")

guess_count = 0
while guess_count <= 10:
    guess_num = int(input("Guess the number: "))
    guess_count += 1

    if guess_num == 0:
        print("Closing the game!")
        break

    if guess_num < target_number:
        print("You guessed a lower number. Choose a higher number.")
    elif guess_num > target_number:
        print("You guessed a higher number. Choose a lower number.")
    elif guess_num == target_number:
        print("You guessed it right!")
        break

else: 
    print(f"You failed to guess the target number. The target number was {target_number}.")
    print("Try again!")
    
