'''
A computer manufacturing company has the following monthly compensation policy to their sales-person.
Minimum base salary : 1500.00
Bonus for every computer sold : 200.00
Commission on the total monthly sales : 2 per cent
Given the base salary ,bonus, and commission rate, the inputs necessary to calculate the gross
salary are, the price of each computer and the number sold during the month
The gross salary is given by the equation|:
Gross salary=base salary+(quantity*bonus rate) + (quantity*price)*commission
'''
bsl = float(input("Enter the Salary: "))
bon = float(input("Enter the Bonus rate for every computer sold: "))
com = float(input("Enter Commission on total monthly sales in percentage: "))
qun = int(input("Enter the Quantity as per items: "))
gross_sal = bsl + (qun * bon) + (qun * bsl) * com
print("Gross salary for employee: ", gross_sal)