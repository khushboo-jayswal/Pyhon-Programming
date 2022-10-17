'''
Fibonacci series 0,1,1,2,3,5,8,13,21,34,...
'''
n1, n2 = 0, 1
count = 0
nterm = int(input("Enter the n term for Fibonacci: "))
if nterm <= 0:
    print("Please enter the Positive integer")
elif nterm == 1:
    print("Fibonacci sequence upto: ", n1)
else:
    print("Fibonacci sequence: ")
    while count < nterm:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1