#------------- user login functions

def first_name():
    while True:
        print()
        f_name = input("First Name: ")
        # if user enters alphabetic letters for name variable
        if f_name.isalpha():
            # checks length of name
            name_count = len(f_name)
            if f_name == "q":
                exit()
            elif name_count < 3:
                print()
                print("Name length too short, try again.")
                # end of if, but still in while loop
            # so if name is letter and more then 3 characters break the while loop
            else:
                # returns name and makes first letter a captial
                return f_name.capitalize()
                break
        # if name isn't in letters then: (still in while loop, so will ask for input again)
        else:
            print()
            print("Please enter your name")


def last_name():
    while True:
        print()
        l_name = input("Last Name: ")
        # if user enters alphabetic letters for name variable
        if l_name.isalpha():
            # checks length of name
            name_count = len(l_name)
            # if the length is less then 3 characters, display error
            if l_name == "q":
                exit()
            elif name_count < 3:
                print()
                print("Name length too short, try again.")

                # end of if, but still in while loop
            # so if name is letter and more then 3 characters break the while loop
            else:
                # returns name and makes first letter a captial
                return l_name.capitalize()
                break
        # if name isn't in letters then: (still in while loop, so will ask for input again)
        else:
            print()
            print("Please enter your name")


def age_check():
    while True:
        try:
            print()
            age = int(input("Age: "))
            if age < 13:
                print()
                print("Sorry you are not eligible to register.")
                exit()
            else:
                return age

        # if user enters string instead of integar (age)
        except ValueError:
            print()
            print("Invalid Value Entered")
            print()


def email_check():
    while True:
        print()
        # research module imported
        import re
        # email format includes (names/numbers/symbols[@]+[.])
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        email = input("Email Address: ")
        # checking format
        if(re.search(regex,email)):
            return email
            break
        else:
            print()
            print("Invalid Email")


def username_check():
    while True:
        print()
        username = input("Username: ")
        if len(username) < 8:
            print("Username must be at least 8 characters")
        # if space is included
        elif " " in username:
            print("Username must not include spaces")
        else:
            return username
            break


# RETURN HASH VALUE (ENCRYPT)
def password_check():
    while True:
        print()
        password = input("Password: ")
        if len(password) < 8:
            print("Password too short!")
        # if space is included
        elif " " in password:
            print("Password must not include spaces")
        else:
            return password
            break
