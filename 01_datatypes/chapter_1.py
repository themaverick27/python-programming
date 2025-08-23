# immutable

sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Updated sugar: {sugar_amount}")

# check identity of each value
print(f"ID of sugar_amount value 2: {id(2)}")
print(f"ID of upated sugar_amount value 12: {id(12)}")

# identity changed, new memory created for the new values i.e new memory reference (identity changed) - immutable 
# immutable because the old value remained in the memory, new memory reference created for the new value, still the old value is not changed and is in the memory, reference changed, that's why immutable. 

