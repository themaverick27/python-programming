# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

user_age = int(input("enter your age: "))
day = input("enter today day: ")

total_price = 0
if(user_age < 18):
    total_price += 8
else:
    total_price += 12

if(day.lower() == "wednesday"):
    total_price -= 2

print(total_price)