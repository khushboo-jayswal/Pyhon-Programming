import random
import string

# Random string for one character and one letter
b = []
for i in range(10):
    b.append(i)
a = []
for i in range(65, 91):
    a.append(chr(i))
c = ""
for i in range(6):
    if i % 2 == 0:
        c = c + str(random.choice(b))
    else:
        c = c + random.choice(a)
print("Randon string for one ch and one letter :", c)

# Random string of fixed length
def random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

random_string(8)
random_string(8)
random_string(5)

# Random string of lower case and upper case letters
def rand_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string in Capital-small is :", result_str)

rand_string(8)
rand_string(8)

# Random string of specific letters only
def random_str(length):
    # put your letters in the following string
    sample_letters = 'abcdefghi'
    result_str = ''.join((random.choice(sample_letters) for i in range(length)))
    print("Random string is for specific letters:", result_str)

random_str(5)
random_str(5)

# Random string without repeating characters
def ran_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.sample(letters, length))
    print("Random String without repeating any characters is:", result_str)

ran_string(7)
ran_string(7)

# Random alphanumeric string of letters and digits
def random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("Random alphanumeric String is:", result_str)

random_alphanumeric_string(8)
random_alphanumeric_string(8)

# Random alphanumeric string with a fixed count of letters and digits\
def random_alphanumeric_str(letters_count, digits_count):
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert string to list and shuffle it to mix letters and digits
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

# 5 letters and 3 digits
print("First random alphanumeric string is:", random_alphanumeric_str(5, 3))

# 6 letters and 2 digits
print("Second random alphanumeric string is:", random_alphanumeric_str(6, 2))

# Random password string with Special characters, letters, symbols and digits

def random_password_string(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    print("Random string password is:", password)

random_password_string(10)
random_password_string(10)
import random
import string

def random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(6):
        password += random.choice(random_source)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

print("First Random Password is ", random_password())
print("Second Random Password is ", random_password())

# secure Random string and password
import secrets

def secure_random_string(length):
    secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(length)))
    return secure_str

print("First secure random String is:", secure_random_string(8))
print("Second secure random String is:", secure_random_string(8))
# secrets module to generate a secure token string
print("Secure hexadecimal string token:", secrets.token_hex(32))

# UUID module to generate Universally Unique secure random String Id
import uuid
stringId = uuid.uuid4()
print("Secure unique string id:", stringId)

# StringGenerator module to generate a random string
# import strgen
# randomString = strgen.StringGenerator("[\w\d]{10}").render()
# print("random string using StringGenerator", randomString)
# randomString = strgen.StringGenerator("[\d]{3}&[\w]{3}&[\p]{2}").render()
# print("random string using StringGenerator", randomString)

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = eval(input("Enter a month number (1-12): "))
pos = (n-1) * 3
monthAbbrev = months[pos:pos+3]
print("The month abbreviation is", monthAbbrev + ".")