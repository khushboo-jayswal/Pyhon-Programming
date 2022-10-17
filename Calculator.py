'''  Write a python program will keep adding a stream of numbers inputted by user. The adding stops as soon as user process
q key on the keyboard  '''

# sum = 0
# while(True):
#     userInput = input("Enter the Item price or press q to quit: \n")
#     if(userInput != 'q'):
#         sum = sum + int(userInput)
#         print(f"Order total so far: {sum}")
#
#     else:
#         print(f"Your Total Bill is: {sum}. Thanks for shopping with us...")
#         break

a = float(input("Enter the num 1: "))
b = float(input("Enter the num 2: "))
def sum(a, b):
    ans = a + b
    print(f"The sum of {a} and {b} is: {ans}")
sum(a, b)

def sub(a, b):
    if a > b:
        ans = a - b
    else:
        ans = b - a
    print(f"The sub of {a} and {b} is: {ans}")
sub(a, b)

def mul(a, b):
    ans = a * b
    print(f"The mul of {a} and {b} is: {ans}")
mul(a, b)

def resto(a, b):
    ans = a ** b
    print(f"The power of {a} and {b} is: {ans}")
resto(a, b)

def div(a, b):
    ans = a / b
    print(f"The div of {a} and {b} is: {ans}")
div(a, b)

def flr(a, b):
    ans = a // b
    print(f"The floor of {a} and {b} is: {ans}")
dev(a, b)

def mod(a, b):
    ans = a % b
    print(f"The module of {a} and {b} is: {ans}")
mod(a, b)