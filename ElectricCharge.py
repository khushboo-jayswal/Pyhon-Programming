'''
An electric power distribution company charges its domestic consumers as follows:
consumption Units Rate of Charge
0-200 Rs. 0.50 per unit
201-400 Rs. 100 plus Rs. 0.65 per unit excess of 200
401-600 Rs. 230 plus Rs. 0.80 per unit excess of 400
601 and above Rs. 390 plus Rs. 1.00 per unit excess of 600
this program reads the customer number and power consumed and points the amount to be paid
by the customer.
'''
unit = int(input("Enter the units: "))
if unit > 0 and unit <= 200:
    price = unit * 0.50
elif unit > 200 and unit <= 400:
    price = 100 + (unit - 200) * 0.65
elif unit > 400 and unit <= 600:
    price = 230 + (unit - 400) * 0.80
elif unit > 600:
    price = 390 + (unit - 600) * 1
else:
    print("Enter wrong input..")
print("Price is: " + str(price))