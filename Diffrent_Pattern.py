# Diamond
p1 = int(input("Enter rows for p1:"))
a = 2 * p1 - 2
for i in range(0, p1):
    for j in range(0, a):
        print(end=" ")
    a = a - 1
    for j in range(0, i+1):
        print("* ", end="")
    print("")
a = p1 - 2
for i in range(p1, -1, -1):
    for j in range(a, 0, -1):
        print(end=" ")
    a = a + 1
    for j in range(0, i+1):
        print("* ", end="")
    print("")

print("\n")
# Diamond Star
for i in range(5):
    for j in range(5):
        if i+j == 2 or i-j == 2 or i+j == 6 or j-i == 2:
            print("*", end="")
        else:
            print(end=" ")
    print("")

print("\n")
# K Pattern
for i in range(7):
    for j in range(7):
        if j == 0 or i - j == 3 or i + j == 3:
            print("*", end=" ")
        else:
            print(end=" ")
    print("")

print("\n")
p2 = int(input("Enter row p2:"))
for i in range(1, p2+1, 1):
    for j in range(1, p2+2-i, 1):
        print(j, end="")
    print("")
for i in range(2, p2+1, 1):
    for j in range(1, i+1, 1):
        print(j, end="")
    print("")

print("\n")
p3 = int(input("Enter row p3:"))
for i in range(1, p3+1, 1):
    for j in range(1, i+1, 1):
        print(j, end=" ")
    for k in range(1, i, 1):
        print(k, end=" ")
    print("")

print("\n")
p4 = int(input("Enter row p4:"))
for i in range(0, p4, 1):
    for j in range(1, p4, 1):
        if i == j:
            print(j, end="")
        else:
            print("0", end="")
    print("")

print("\n")