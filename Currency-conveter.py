with open('currencyData.txt') as f:
    lines = f.readlines()

for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter the Amount: "))
print("Enter the Name of currency want to convert amount to? Available options\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of the values: ")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")
