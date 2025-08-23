import sys

# Real numbers - precision in numbers

ideal_temp = 95.5
current_temp = 95.499999999999

print(f"Ideal temperature: {ideal_temp}")
print(f"Current temperature: {current_temp}")

print(f"Difference temperature: {ideal_temp - current_temp}")


print(sys.float_info)

# when you want to deal with large numbers or complex calculations, use packages or libraries. 
