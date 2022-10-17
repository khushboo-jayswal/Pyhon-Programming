print("Convert Celsius to Fahrenheit")
cel = float(input("Enter temperature in celsius: "))
fer = (cel * 9/5) + 32
print(fer)
kel = 273.5 + (fer - 32) * 5/9
print(kel)

print("Convert Fahrenheit to Celsius")
fer = float(input("Enter temperature in fahrenheit: "))
cer = (fer - 32) * 5/9
print(cer)