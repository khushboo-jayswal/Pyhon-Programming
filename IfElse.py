'''
write a program to find out if the driver is insured or not.A company insures its drivers in the following cases:
1: if driver is married
2: if driver is unmarried, male and above 30 yrs.
3: if driver is unmarried, female and above 25 yrs.
write a program to find out if the driver is insured or not.
'''
ms = input("Enter the Marital Status M or U: ")
gen = input("Enter Gender M or F: ")
age = int(input("Enter Age: "))
if ms == "M":
    print("Insured")
elif ms == "U" and gen == "M" and age > 30:
    print("Insured")
elif ms == "U" and gen == "F" and age > 25:
    print("Insured")
else:
    print("Not Insured")