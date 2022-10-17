print("1 + 2 + 3 + ... + N")
sum = 0
i = 1
n = int(input("Enter the num: "))
if n <= 0:
    print("Enter only Positive num")
else:
    while i <= n:
        sum = sum + i
        i = i + 1
    print("Addition of specific range in series is: ", sum)

print("1 - 2 + 3 - 4 + ... - N + (N+1) [Odd +, Even -]")
no = int(input("Enter the num: "))
j = 1
s = 0
while j <= no:
    if j % 2 == 0:
        s = s - j
    else:
        s = s + j
    j = j + 1
print("Series is:", s)

print("1^2 + 2^2 + 3^2 + ... + n^2")
num = int(input("Enter only Positive number: "))
tot = 0
while tot > 0:
    tot = (num * (num + 1) * (2 * num + 1)) / 6
print("Sum of series is: {0} = {1}".format(num, tot))
'''
for i in range(1, num + 1):
    if i != num:
       print("%d^2 + " %i, end = ' ')
    else:
       print("{0}^2 = {1} ".format(i, tot))
'''

print("1/2 + 3/4 +5/6 + ... + N/N+1")
n = int(input("Enter the number: "))
np = 0
for each in range(1, n+1):
    np = np + (each/(each+1))
print("Computed value: ", format(round(n, 2)))

print("1/1! + 2/2! +3/3! + ... + n/n!")
def sumOfSeries(ns):
    res = 0
    fact = 1
    for k in range(1, ns+1):
        fact *= k
        res = res + (k / fact)
    return res
nu = int(input("Enter the num: "))
print("Sum is: ", sumOfSeries(nu))

print("1/2! + 2/3! +3/4! + ... + n/(n+1)!")
numb = int(input("Enter the number: "))
r = 0
fac = 1
while (numb+1) > 0:
    fac *= (numb + 1)
    r = r + (numb / fac)
print("Addition of series is: ", r)
