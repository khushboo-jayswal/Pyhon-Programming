# This is single line comment
''' Multi line comment '''
#import math
#print (math.gcd(3,6))

'''
a = 34
b = "Knight"
c = 45.32
d = 2

print(a + d)
print(a - d)
print(a * d)
print(a / d)
print(a ** d)    # Exponentiation
print(a // d)    # Floor division
print(a % d)
'''

'''
         Rules for Variables
         1. It should be start with a letter or underscore
         2. It cannot start with a number
         3. It can only contain alpha numeric characters
         4. Variables are case sensitive : Har har different


typeA = type(a)
typeB = type(b)
print(typeA)
print(typeB)
'''


#Type_Casting
'''
e = "31"
print(type(e))
print(int(e))
print(float(e))

f = 2
print(type(f))
print(str(f))
print(float(f))

g = 3.5
print(type(g))
print(str(g))
print(int(g))
'''

'''
name = "It, is, my First Experience."
print(name[0])
print(name[1:4])        # index 1-3 letter print
print(name.strip())     # Remove extra space
print(len(name))        # Length
print(name.lower())     # Lowercase
print(name.upper())     # Uppercase
print(name.capitalize())   # First letter Capital
print(name.swapcase())     # Swap lower to upper and upper to lower
print(name.replace("is", "it"))    # Replace
print(name.replace(",", "_"))
'''

'''
str1 = "This is a "
name = "Khush"
frd = "Mrunali"
str2 = "This is not a "
print(str1 + name)
temp = "This is a {} and its friend name was {}.".format(name, frd)
r = "This is a {0} and its friend name was {1}.".format(name, frd)
k = "This is a {1} and its friend name was {0}.".format(name, frd)
print(temp, "\n", r, "\n", k)
print(f"This is a {name} and its friend name was {frd}.")
'''

'''
          Python Collsections:
          1.List(Change the item)      2.Tuples(Not change the item, if change then convert in list)
          3.Set(Not repeat item)        4.Dictionary
'''

'''
lst = [1,43,2,34,3,6]
print(type(lst))
lst[2] = 8
lst.append(20)        # Add item at end in list
lst.insert(2,24)      # Add item at specific in list
lst.pop()             # Delete item at end in list
lst.remove(1)         # Delete item at specific in list
del lst[3]            # Delete item at specific index
print(lst[1:4])
print(lst)
print(len(lst))
lst.clear()        
'''

'''
tup = ("Apple", "Orange", "Mango")
tup = list(tup)
tup[0] = "Banana"
print(type(tup))
tup.append("Chiku")        # Add item at end in tuple
tup.insert(2,"Lamon")      # Add item at specific in tuple
tup.pop()                  # Delete item at end in tuple
tup.remove(tup[1])         # Delete item at specific in tuple
del tup[2]                 # Delete item at specific tuple
print(tup[1:3])
print(tup)
print(len(tup))
'''

sat = {23, 2, 2, 2, 4, 56, 4, 7, 3, 7, }
print(type(sat))
set.append("AP")