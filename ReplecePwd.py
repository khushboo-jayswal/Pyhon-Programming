# BlackB0ard$123
# blackAndWhite --> black$&white$
SECURE = (('s', '$'), ('and', '&'), ('a', '@'), ('0', '*'), ('i', '1'), ('I', '|'))

def securePwd(password):
    for a, b in SECURE:
        password = password.replace(a, b)
    return password

if __name__ == '__main__':
    password = input("Enter Password: ")
    password = securePwd(password)
    print(f"Your Secure Password is {password}")