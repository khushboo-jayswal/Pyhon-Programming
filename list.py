a = []
n = int(input("Enter Total num of elements:"))
for i in range(n):
    item = int(input("Enter element: "))
    a.append(item)
for i in range(n):
    print("a[" + str(i) + "] = " + str(a[i]))

sum = 0
for i in range(n):
    sum = sum + a[i]
print("The sum of list is:", str(sum))

max = 0
min = 0
for i in range(n):
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]
print(f"The Max no is:{max} and Min no is:{min} in list")

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t = ['d', 'c', 'e', 'b', 'a']
print(t.sort())
# print(t.find('a'))

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
stack.pop()
print(stack)

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")          # Terry arrives
queue.append("Graham")         # Graham arrives
print(queue)
queue.popleft()
queue.popleft()
print(queue)
queue.pop()      # Popright
print(queue)