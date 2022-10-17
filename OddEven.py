print("ODD - EVEN")
num = int(input("Enter the number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

print("POSITIVE - NEGATIVE")
n = int(input("Enter the number: "))
if n > 0:
    print(f"{n} is Positive")
elif n == 0:
    print("Zero")
else:
    print(f"{n} is Negative")

print("SUM OF ODD-EVEN")
ran = int(input("Enter the Maximum range: "))
evens = 0
odds = 0
for ran in range(1, ran+1):
    if ran % 2 == 0:
        evens += ran
    else:
        odds += ran
print("Sum of Even no is: {0} = {1}".format(ran, evens))
print("Sum of Odd no is: {0} = {1}".format(ran, odds))