# Problem: Suggest an activity based on the weather 
# (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input("enter weather condition: ")

if weather.lower() == "sunny":
    activity = "Go for a walk!"
elif weather.lower() == "rainy":
    activity = "Read o book!"
elif weather.lower() == "snowy":
    activity = "build a snowman!"

print(activity)