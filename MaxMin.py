print("TERNARY / CONDITIONAL OPERATOR")    # (false, true) [Condition]
a = int(input("Enter the 1st num: "))
b = int(input("Enter the 2nd num: "))
max = (b, a)[a > b]  # max = a if a>b else b
min = (b, a)[a < b]
print(f"Max is {max} and min is {min}: ")

a1 = int(input("Enter the 1st num: "))
b1 = int(input("Enter the 2nd num: "))
c1 = int(input("Enter the 3rd num: "))
max = ((c1, b1)[b1 > c1], (c1, a1)[a1 > c1])[a1 > b1]
print("Max is: ", max)