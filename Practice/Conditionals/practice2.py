# if elif else ladder

# Take the input of temperature in celsius.
''' Below 0°C → "Freezing Cold b
0°C to 10°C → "Very Cold b
10°C to 20°C → "Cold b
20°C to 30°C → "Pleasant b
30°C to 40°C → "Hot b
Above 40°C → "Very Hot " '''


temperature = float(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("Freezing Cold")
elif temperature < 10:
    print("Very Cold")
elif temperature < 20:
    print("Cold")
elif temperature < 30:
    print("Pleasant")
elif temperature < 40:
    print("Hot")
else:
    print("Very Hot")