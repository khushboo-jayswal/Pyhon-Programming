a = int(input("Enter Sub1 marks out of 100: "))
b = int(input("Enter Sub2 marks out of 100: "))
c = int(input("Enter Sub3 marks out of 100: "))
t = a + b + c
avg = t / 300
per = float(avg) * 100
print("Avg is: %.2f" % avg)
print(f"Student Percentage is: {float(per)}%")
if per >= 90:
    print("A Grade")
elif per >= 80 and per <= 89:
    print("B Grade")
elif per >= 70 and per <= 79:
    print("C Grade")
elif per >= 60 and per <= 69:
    print("D Grade")
elif per >= 50 and per <= 69:
    print("E Grade")
else:
    print("F Fail")