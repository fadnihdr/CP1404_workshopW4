
def get_number(lower=10,upper=50):
    user_input = input("Enter Enter a number {}-{}".format(lower, upper))
    while True:
        if user_input.isdecimal() == True:
            if int(user_input) >= lower and int(user_input) <= upper:
                for i in range(int(user_input), 120, 11):
                    print("{} {}").format(i,chr(i)).strip()
                break
            else:
                    print("Enter a valid number!")
                    user_input = input("Enter Enter a number {}-{}".format(lower, upper))
        else:
            print("Enter a valid number!")
            user_input = input("Enter Enter a number {}-{}".format(lower, upper))


get_number()




