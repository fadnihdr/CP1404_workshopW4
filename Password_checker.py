import string

print("Your password must be between 5 and 15 characters, and contain:")
print("\t1 or more uppercase characters")
print("\t1 or more lowercase characters")
print("\t1 or more numbers")
print("\tand 1 or more special charcaters: !@#$%^&*()_+[]\{}|;:/~")
password = input("Please enter a valid password:")

upper = string.ascii_uppercase
lower = string.ascii_lowercase
number = string.digits
symbol = string.punctuation

while True:
    if len(password) < 5:
        print("Your password is too short!")
        password = input(">")
    elif len(password) > 15:
        print("Your password is too long!")
        password = input(">")
    elif password is not password in upper:
        print("1.Invalid Password!")
        password = input(">")
    elif password is not password in number:
        print("1.Invalid Password!")
        password = input(">")
    elif password is not password in lower:
        print("2.Invalid Password!")
        password = input(">")
    elif password is not password in symbol:
        print("3.Invalid Password!")
        password = input(">")
    else:
        print(str("Your {} character password is valid: {}").format(len(password),password))
        break
"""
for each in password:
    if each in upper:
        print("true")
"""