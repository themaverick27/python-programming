# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), > 10 chars (Strong).

password = input("enter your password: ")

count_chars = len(password)

if count_chars < 6:
    password_strength = "Weak"
elif count_chars < 11:
    password_strength = "Medium"
else: 
    password_strength = "Strong"

print(password_strength)