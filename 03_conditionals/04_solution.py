# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
fruit_color = "Yellow"

if fruit.lower() == "banana":
    if fruit_color.lower() == "green":
        print("Unripe")
    elif fruit_color.lower() == "yellow":
        print("Ripe")
    elif fruit_color.lower() == "brown":
        print("Overripe")
