# STAR * PATTERN
a = int(input("Enter rows: "))
for i in range(a):
    for j in range(i+1):
        print("*", end="")
    print("")

b = int(input("Enter rows: "))
for i in range(b):
    for j in range(b-i, 0, -1):
        print("*", end="")
    print("")

k = int(input("Enter rows: "))
for i in range(k):
    for j in range(0, k-1):
        print("*", end="")
    print("")

m = int(input("Enter rows: "))
n = 2 * m - 2
for i in range(0, m):
    for j in range(0, n):
        print(end=" ")
    n = n - 2
    for j in range(0, i+1):
        print("* ", end="")
    print("")

q = int(input("Enter rows: "))
for i in range(0, q):
    for j in range(0, i+1):
        print("*", end="")
    print("")
for i in range(q, 0, -1):
    for j in range(0, i-1):
        print("*", end="")
    print("")

r = int(input("Enter rows: "))
s = 2 * r - 2
for i in range(q, -1, -1):
    for j in range(s, 0, -1):
        print(end=" ")
    s = s + 1
    for j in range(0, i+1):
        print("*", end=" ")
    print("")

t = int(input("Enter rows: "))
u = 2 * t - 2
for i in range(0, t):
    for j in range(0, u):
        print(end=" ")
    u = u - 1
    for j in range(0, i+1):
        print("*", end=" ")
    print("")

v = int(input("Enter rows: "))
for i in range(0, v):
    for j in range(0, i+1):
        print("* ", end=" ")
    print("")
for i in range(v, 0, -1):
    for j in range(0, i+1):
        print("* ", end=" ")
    print("")

w = int(input("Enter rows w: "))
x = 2 * w - 2
for i in range(0, w-1):
    for j in range(0, x):
        print(end="")
    x = x - 2
    for j in range(0, i+1):
        print("* ", end="")
    print("")
x = -1
for i in range(w-1, -1, -1):
    for j in range(x, -1, -1):
        print(end="")
    x = x + 2
    for j in range(0, i+1):
        print("* ", end="")
    print("")

# NUM PATTERN
c = int(input("Enter rows: "))
for i in range(c):
    for j in range(i+1):
        print(i+1, end="")
    print("")

d = int(input("Enter rows: "))
for i in range(d):
    for j in range(d-i, 0, -1):
        print(i+1, end="")
    print("")

e = int(input("Enter rows: "))
for i in range(e):
    for j in range(e-i, 0, -1):
        print(e-i, end="")
    print("")

f = int(input("Enter rows: "))
n = 1
for i in range(f):
    for j in range(i+1):
        print(n, end="")
        n = n + 1
    print("")

g = int(input("Enter rows: "))
for i in range(g):
    for j in range(i+1):
        print(g-i-1, end="")
    print("")

h = int(input("Enter rows: "))
for i in range(1, h+1):
    for j in range(1, h-i+1):
        print(j, end="")
    print("")

o = int(input("Enter rows: "))
for i in range(o, 0, -1):
    for j in range(0, i+1):
        print(j, end="")
    print("")

p = int(input("Enter rows p: "))
for i in range(1, p):
    for j in range(p, 0, p-i+j+1):
        print(j, end=" ")
    print("")

