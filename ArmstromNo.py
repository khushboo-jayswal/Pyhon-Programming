n = int(input("Enter No: "))
sum = 0
order = len(str(n))
cpy_n = n
while n > 0:
    digit = n % 10
    sum += digit ** order
    n = n // 10

if sum == cpy_n:
    print(f"{cpy_n} is an armstrong number")           # 153, 371
else:
    print(f"{cpy_n} is not an armstrong number")       # 8891, 34