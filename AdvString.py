
s = input("Enter the String: ")

# SLICING
print(s[0])
print(s[0:3])
print(s[0:5])
print(s[:6])
print(s[-3:-6])   # Nothing is print bcz -3>-6  3<6
print(s[-3:-1])
print(s[-3:])

# STRING
m = "i love %s and %s" % ("Ice-cream", "Chocolates")
print(m)
n = "i love {} and {}".format("Panipuri", "Pizza")
print(n)
o = "i love {1} and {0}".format("Sandwich", "Smoothies")
print(o)

# AFTER PINT SOME VALUE LIKE ROUND OF
staff = " :%.0f" % (2000)
st = " :%.2f" % (2000)
print(f"Staff have {staff} and St have {st}")

# SPLIT  JOIN  REPLACE
sen = "I will be with u till the end of time"
print(sen.split(" ", 1))
print(sen.split(" ", 3))
print(sen.split(" "))
j = "ring, earing, pant, top"
a, b, c, d = j.split(",")
print(f"a = {a} b = {b} c = {c} d = {d}")
print("--".join(sen))
print("-->>>".join(sen))
print("+".join("124587"))
print(j.replace("pant", "plaza"))
print(j.replace("top", "shirt"))

print(ord("A"))  # Ascii val of character
print(chr(69))   # Convert ascii to character

# eval(for Integer and Float datatype)
n = eval(input("Enter no: "))
print(type(n))

s = "Khush is the best"
j = "boo"
print(len(s))        # Lengh
print("".join(s+j))  # Concate
print(s.lower())
print(s.upper())
print(s.title())

# Count no of Words, Characters and Spaces
sr = input("Enter string to count total character and words in string: ")
char = word = sp = 0
for i in range(0, len(sr)):
    char = char + 1     # if sr[i] != '':
    if sr[i] == ' ':
        sp = sp + 1
        word = sp + 1
print("Total no of Characters in string:" + str(char))
print("Total no of Words in string:" + str(word))
print("Total no of Space in string:" + str(sp))

# Count no of Alphabets, Digits and Special characters[!@#$%^&*() ]
s = input("Enter string to count Alphabets, Digits and Special characters(include space): ")
alpha = digit = special = 0
for i in range(len(s)):
    if s[i].isalpha():
        alpha = alpha + 1
    elif s[i].isdigit():
        digit = digit + 1
    else:
        special = special + 1
print("Total no of Alpha in string: ", str(alpha))
print("Total no of Digits in string: ", str(digit))
print("Total no of Special characters in string: " + str(special))

stg = input("For Palindrome enter string:")
def isPalindrome(stg):
    return stg == stg[::-1]
ans = isPalindrome(stg)
if ans:
    print(f"{stg} is palindrome.")
else:
    print(f"{stg} is not palindrome.")

sin = input("Enter String1: ")
cos = input("Enter String2: ")
if sin == cos:
    print(f"{sin} and {cos} are equal.")
else:
    print(f"{sin} and {cos} are not equal.")