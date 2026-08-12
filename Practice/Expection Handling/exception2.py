age = int(input("Enter your age: "))

#if age < 18:
#    raise ValueError("You age must be greater than 18 to vote!")
#else:
#    print("You are allowed to vote!")

#print("Voting is going on!") # if raise executed (based on condition), this statement will not execute, as the program execution will stop there only.


# Solution, if you want the flow of program should not be stopped

age = int(input("Enter your age: "))

try: 
    if age < 18:
        raise ValueError("You age must be greater than 18 to vote!")
    else:
        print("You are allowed to vote!")
except Exception as e:
    print(f"Error occurred: {e}")

print("Voting is going on!")