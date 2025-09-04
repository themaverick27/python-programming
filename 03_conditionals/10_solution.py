# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_species = input("enter pet: ")
pet_age = int(input("enter pet age: "))

if pet_species.lower() == "dog":
    if pet_age < 2:
        pet_food = "Puppy food"
    else:
        pet_food = "Adult food"

elif pet_species.lower() == "cat":
    if pet_age <= 5:
        pet_food = "Junior cat food"
    else:
        pet_food = "Senior cat food"


print(pet_food)