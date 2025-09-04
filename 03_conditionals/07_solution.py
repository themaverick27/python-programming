# Problem: Customize a coffee order: 
# "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("enter your order size (small, medium, large): ")
extra_shots = True

if extra_shots:
    coffee = order_size + " coffee with an extra shots"
else:
    coffee = order_size + " coffee"

print("Order:", coffee)