def happy():
    print("Happy Birthday to You!")
def sing(person):
    happy()
    happy()
    print("Happy Birthday, Dear", person + ".")
    happy()
def _main():
    sing("Fred")
    print()
    sing("Lucy")
_main()

def printline():
    print("--------------------------")
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def main():
    a = eval(input("Enter A:"))
    b = eval(input("Enter B:"))
    print("Enter 1 for Addition\n Enter 2 for Subtraction\n Enter 3 for Multiplication\n Enter 4 for "
          "Division\n ")
    c = eval(input("Enter Your Choice: "))
    printline()
    if c == 1:
        print("Addition: ", add(a, b))
    elif c == 2:
        print("Subtraction: ", sub(a, b))
    elif c == 3:
        print("Multiplication: ", mul(a, b))
    elif c == 4:
        print("Division: ", div(a, b))
    else:
        print("Invalid choice")
main()