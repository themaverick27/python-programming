# Boolean - True (1) and False (0)

is_boiling = True
stir_count = 5

total_actions = stir_count + is_boiling  # upcasting
print(f"total actions: {total_actions}") 

book_present = 0 # not present (false)
print(f"Is there book? {bool(book_present)}")


copy_present = 1 # present (true)
print(f"Is there copy? {bool(copy_present)}")


# true values - True, 1, "<value>", 12 etc
# false values - False, 0, None

# logical operations 
water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can serve Tea? {can_serve}")

tea_added = True
can_serve = water_hot and tea_added
print(f"Can serve Tea? {can_serve}")
