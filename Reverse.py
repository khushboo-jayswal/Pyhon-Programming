print("REVERSE NO")
n = int(input("Enter the no: "))
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
print("Reverse no is: ", rev)

num = int(input("Enter the number for Reverse no or not:"))
if num == 'x':
    exit()
else:
    ori = num
    rv = 0
    while num > 0:
        rv = (rv * 10) + num % 10
        num //= 10
    if ori == rv:
        print("Original no is same as Reverse", rv)
    else:
        print("Original no is not same as Reverse", rv)