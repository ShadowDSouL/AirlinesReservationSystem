# Tong Sheng Kit
# TP059117


def main_menu():
    print("-" * 50)
    print("         Welcome to Air Malaysia Group")
    print("-" * 50)
    print("                 <Main Menu>")
    print("""Press [1] - to schedule the airline time\n"""
          """Press [2] - to search the airline\n"""
          """Press [3] - to register\n"""
          """Press [4] - to login\n"""
          """Press [5] - to exit the program""")
    print("-"*50)


def get_option():
    print(" ")
    print("""Press [1] - to schedule the airline time\n"""
          """Press [2] - to search the airline\n"""
          """Press [3] - to register\n"""
          """Press [4] - to login\n"""
          """Press [5] - to exit the program\n """)


def newacc(new_acc, new_pass): # add new account and create profile
    for i in range(1, 5):
        print("Please create your profile")
        name = input("Enter your name: ")
        dob = input("Enter your date of birth: ")
        mobile = input("Enter your phone number: ")
        citizenship = input("Enter your citizenship: ").upper()
        passport = input("Enter your passport number: ")
        emergency = input("Enter emergency contact: ")
        card = input("Enter your credit or debit card number: ")
        if name and dob and mobile and citizenship and passport and emergency and card: # empty input is not allow
            with open("members.txt", "a") as mem:
                mem.write(new_acc + "," + new_pass + "," + name + "," + dob + "," + mobile + "," + citizenship + "," +
                          passport + "," + emergency + "," + card + "\n")
                print("Completed !!" + "\n")
            break
        else:
            print("Please complete your information !!")
            if i < 4: # if the username is used then it will have 4 change to redo
                print(f"You still have {4 - i} change")

            else:
                print("Page terminated!!")


def check_acc(new_acc): # check account in the txt
    with open("members.txt", "r") as mem:
        for line in mem:
            line = line.rstrip()
            if line.startswith(new_acc):
                return 1


def display_schedule():
    with open("airline.txt", "r") as schedule:
        print("-" * 150)
        print(" " * 90, "Departure", " " * 15, "Return")
        print("Flight number :", " " * 14, "From", " " * 33, "To", " " * 15, "Date     Time(GMT+8)", " " * 3,
              "Date     Time(GMT+8)", "     Price")
        print("-" * 150)
        for line in schedule.readlines():
            line = line.rstrip()
            line = line.split(",")
            num1 = len(line[1])
            num2 = len(line[2])
            num3 = len(line[3])
            num4 = len(line[4])
            space1 = 16 - num1
            space2 = 16 - num2
            space3 = 16 - num3
            space4 = 16 - num4
            print(" " * 3 + line[0] + "     : " + (" " * space1) + line[1] + " - " + line[2] + (" " * space2) + "->" +
            (" " * space3) + line[3] +" - " + line[4] + (" " * space4) + line[5] + "    " + line[6] + "    |   " + line[7]
            + "    " + line[8] + "         RM " + line[9])
        print("-" * 150)


def option1(): # display flight
    print("-" * 150)
    print(" " * 125 + "Search")
    print("-" * 150)
    display_schedule()
    print(" " * 125 + "Main Menu")
    print("-" * 150)


def option2(): # search flight
    flight = (input("Please insert the country you want:")).upper()
    date = (input("Please insert the date you want:")).upper()
    print("-" * 150)
    count = 0
    with open("airline.txt", "r") as search:
        print("-" * 150)
        print(" " * 90, "Departure", " " * 15, "Return")
        print("Flight number :", " " * 14, "From", " " * 33, "To", " " * 15, "Date     Time(GMT+8)", " " * 3,
              "Date     Time(GMT+8)", "     Price")
        print("-" * 150)
        for line in search.readlines():
            line = line.rstrip()
            line = line.split(",")
            num1 = len(line[1])
            num2 = len(line[2])
            num3 = len(line[3])
            num4 = len(line[4])
            space1 = 16 - num1
            space2 = 16 - num2
            space3 = 16 - num3
            space4 = 16 - num4
            if flight in line or date in line:
                print(" " * 3 + line[0] + "     : " + (" " * space1) + line[1] + " - " + line[2] + (" " * space2)+ "->"
                      + (" " * space3) + line[3] + " - " + line[4] + (" " * space4) + line[5] + "    " + line[6]
                      + "    |   " + line[7] + "    " + line[8] + "         RM " + line[9])
                count = 1  # condition to prove it finds the data

        if count == 0: # if count = 0 then means nothing found in the txt
            print("---------------------------------------------------------------NO FLIGHT------------------------------------------------------------------------------")


def option3(): # register
    print("Please insert a username and password to create an account")
    print("-"*100)
    for i in range(1, 5):
        new_acc = input("Please insert your username:")
        new_pass = input("Please insert your password:")
        new_pass2 = input("Please insert your password again:")
        c = check_acc(new_acc)
        if c != 1 and new_pass == new_pass2: # If c is not 1 and new password is same then it will write the account
            # and password and profile information into the txt
            print("Congratulations on your successful registration")
            newacc(new_acc, new_pass)
            break
        else:
            print("Username has been used or Password incorrect")
            if i < 4: # if the username is used then it will have 4 change to redo
                print(f"You still have {4 - i} change")

            else:
                print("Page terminated!!")


def check(acc, password): # check login account
    if acc == "admin" and password == "admin123":  # checking account for admin
        return 0
    else:
        with open("members.txt", "r") as mem:
            for line in mem.readlines():
                line = line.rstrip()
                line = line.split(",")
                if acc == line[0]:
                    if password == line[1]:
                        return 1


def option4(admin, member): # login
    count = 0
    for i in range(1, 4):
        acc = input("Please enter your username:")
        password = input("Please insert your password:")
        c = check(acc, password)
        if c == 0:  # Check account, login as admin
            print("-" * 50)
            print("             Welcome back Admin!")
            print("-" * 50)
            count = 1
            break
        elif c == 1:  # Check account, login as member
            print("Login Succeed")
            count = 2
            break
        else:
            print("\nIncorrect username or password")
            if i < 3:
                print(f"You still have another {3 - i} change!!!")
            else:
                print("You are unable to login, please try later")
    if count == 1:
        admin(display_schedule)
        main_menu()
    elif count == 2:
        member(display_schedule, acc)
        main_menu()
    else:
        print("Invalid!")
        main_menu()