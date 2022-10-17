year = int(input("Enter the Year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{0} is a Leap year.".format(year))
        else:
            print("{0} is not a Leap year.".format(year))
    else:
        print("{0} is a Leap year.".format(year))
else:
    print("{0} is not a Leap year.".format(year))