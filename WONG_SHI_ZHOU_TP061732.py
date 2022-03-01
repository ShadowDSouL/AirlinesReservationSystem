# WONG SHI ZHOU
# TP061732

def modify_detail(acc):
    print("-" * 50)
    print("         Modify My Profile Details")
    print("-" * 50)
    with open("members.txt", "r") as modify:
        n = modify.readlines()
        choice = input("Are you sure you want to modify account?" + "\n" +
                       "If yes please insert 'Yes', else please insert 'No' :   ").upper()
        count = 0
        name = []
        c = 0
        if choice == "YES":
            for line in n:
                line = line.rstrip()
                line = line.split(",")
                if acc in line:
                    print(" Name:", line[2] + "\n", "Date of birth:", line[3] + "\n", "Phone Number:", line[4] + "\n",
                          "Citizenship:", line[5] + "\n", "Passport:", line[6] + "\n", "Emergency Contact:", line[7] +
                          "\n", "Credit/Debit Card", line[8] + "\n")
                    count = 1

            if count == 0:
                print("Profile not found" + "\n")
            if count == 1:
                with open("members.txt", 'r') as file:
                    for f in file.readlines():
                        c += 1
                        f = f.rstrip()
                        f = f.split(",")
                        name.append(f)

                b = 0
                for y in name:
                    if acc in y:
                        break
                    b += 1
                na = input("Enter your name: ")
                dob = input("Enter your date of birth: ")
                mobile = input("Enter your phone number: ")
                citizenship = input("Enter your citizenship: ").upper()
                passport = input("Enter your passport number: ")
                emergency = input("Enter emergency contact: ")
                card = input("Enter your credit or debit card number: ")

                with open("members.txt", 'w') as prof:
                    for i in range(0, c):
                        if b != i:
                            prof.write(name[i][0])
                            prof.write(",")
                            prof.write(name[i][1])
                            prof.write(",")
                            prof.write(name[i][2])
                            prof.write(",")
                            prof.write(name[i][3])
                            prof.write(",")
                            prof.write(name[i][4])
                            prof.write(",")
                            prof.write(name[i][5])
                            prof.write(",")
                            prof.write(name[i][6])
                            prof.write(",")
                            prof.write(name[i][7])
                            prof.write(",")
                            prof.write(name[i][8])
                            prof.write("\n")
                        else:
                            prof.write(name[i][0])
                            prof.write(",")
                            prof.write(name[i][1])
                            prof.write(',')
                            prof.write(na)
                            prof.write(',')
                            prof.write(dob)
                            prof.write(',')
                            prof.write(mobile)
                            prof.write(',')
                            prof.write(citizenship)
                            prof.write(',')
                            prof.write(passport)
                            prof.write(',')
                            prof.write(emergency)
                            prof.write(',')
                            prof.write(card)
                            prof.write("\n")

        elif choice == "NO":
            print("Page terminated !!" + "\n")
        else:
            print("Incorrect option!!" + "\n")


def display_detail(acc):
    print("-" * 50)
    print("         My Profile")
    print("-" * 50)
    with open("members.txt", "r") as profile:
        for line in profile.readlines():
            line = line.rstrip()
            line = line.split(",")
            if acc in line:
                print("\n Name              :", line[2] + "\n", "Date of birth     :", line[3] + "\n",
                      "Phone Number      :", line[4] + "\n", "Citizenship       :", line[5] + "\n",
                      "Passport          :", line[6] + "\n", "Emergency Contact :", line[7] + "\n",
                      "Credit/Debit Card :", line[8] + "\n")
                print("Successfully read." +"\n")
                break
        else:
            print("Profile not found.")


def my_booking(acc):
    print("-" * 50)
    print("         My Booking")
    print("-" * 50)
    with open("booking.txt", "r") as booked:
        readbooked = booked.read()
        booking_list = readbooked.splitlines()
    master_list = []
    for data in booking_list:
        bookingdata = data.split(",")
        master_list.append(bookingdata)
    for list_in_list in master_list:
        if acc in list_in_list:
            print("+++++++++++++++++++++++++++++++++++++++++++")
            print("----------------------------------")
            print("Invoice ID: ", list_in_list[-1])
            print("----------------------------------")
            print(f"Flight No              : {list_in_list[1]}")
            print(f"Departure Airport      : {list_in_list[2]} - {list_in_list[3]}")
            print(f"Destination Airport    : {list_in_list[4]} - {list_in_list[5]}")
            print(f"Departure Date and time: {list_in_list[6]} {list_in_list[7]}")
            if list_in_list[11] == "round-trip ticket":
                print(f"Return Date and Time   : {list_in_list[8]} {list_in_list[9]}")
            print(f"Ticket type            : {list_in_list[11]}")
            print(f"Adult Ticket           : {list_in_list[13]}")
            print(f"Child Ticket           : {list_in_list[14]}")
            print(f"Flight Class           : {list_in_list[12]}")
            print(f"Seat Type              : {list_in_list[16]}")
            print(f"Insurance number       : {list_in_list[17]}")
            print(f"Total payment          : {list_in_list[18]}")
            print("+++++++++++++++++++++++++++++++++++++++++++")
    else:
        print("No record.")


def book_flight(display_schedule, acc):
    display_schedule()
    from_country = input("Where are you? (Country): ").upper()
    to_country = input("Where you want to go? (Country): ").upper()
    with open("airline.txt", "r") as schedule:
        schedule_list = schedule.readlines()
        print(" " * 90, "Departure", " " * 15, "Return")
        print("Flight number :", " " * 14, "From", " " * 33, "To", " " * 15, "Date     Time(GMT+8)", " " * 3,
              "Date     Time(GMT+8)", "     Price")
        print("-" * 150)
        count = 0
        for line in schedule_list:
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
            if from_country == line[1] and to_country == line[3]:
                print(" " * 3 + line[0] + "     : " + (" " * space1) + line[1] + " - " + line[2] + (" " * space2)
                      + "->" + (" " * space3) + line[3] + " - " + line[4] + (" " * space4) + line[5] + "    " + line[6]
                      + "    |   " + line[7] + "    " + line[8] + "         RM " + line[9])
                count += 1

        if count == 0:
            print("                                                                Country not found!")
        if count >= 1:
            flight_no = input("Enter a flight no: ").upper()
            for line in schedule_list:
                line = line.rstrip()
                line = line.split(",")
                if from_country == line[1] and to_country == line[3]:
                    if flight_no == line[0]:
                        print(f"\nAre you sure you want to select this flight?\n  ")
                        print("+++++++++++++++++++++++++++++++++++++++")
                        print(f"Flight No              : {line[0]}")
                        print(f"Departure Airport      : {line[1]} - {line[2]}")
                        print(f"Destination Airport    : {line[3]} - {line[4]}")
                        print(f"Departure Date and time: {line[5]} {line[6]}")
                        print(f"Return Date and Time   : {line[7]} {line[8]}")
                        print(f"Price                  : RM{line[9]}")
                        print("+++++++++++++++++++++++++++++++++++++++")
                        confirmation = input(""""Y" for Yes, "N" for No: """).upper()
                        data_list = [acc]
                        if confirmation == "Y":
                            with open("booking.txt", "a") as booked:
                                for i in range(10):
                                    data_list.append(line[i])
                                data_list.append(type_f())
                                data_list.append(class_f())
                                data_list.append(adult())
                                data_list.append(child())
                                data_list.append(baggage())
                                data_list.append(seat_type())
                                data_list.append(insurance())
                                data_list.append(total_amount(data_list))
                                data_list.append(payment(data_list))
                                if data_list[-1] == "no confirm":
                                    print("your payment process is cancelled!\n")
                                else:
                                    for data in data_list:
                                        if data == data_list[-1]:
                                            booked.write(data)
                                        else:
                                            booked.write(data + ",")
                                    booked.write("\n")
                                    print("Your flight has been booked successfully. Thank you.\n")
                                    print("Thank you for choosing us.")

                        elif confirmation == "N":
                            print("Your flight booking process is cancelled!")

                        else:
                            print("Invalid input! Your process has been cancelled!")
                        break
            else:
                print("                                                                Flight not found!")


def insurance():
    choice = input("Do you need insurance?\n"
                   "Press [Y] for yes\n"
                   "Press [N] for no\n"
                   "What is your choice?: ").upper()
    insurance_no = "1000"
    if choice == "Y":
        with open("booking.txt", "r") as booked:
            readbooked = booked.read()
            booking_list = readbooked.splitlines()
        master_list = []
        for data in booking_list:
            bookingdata = data.split(",")
            master_list.append(bookingdata)

        for list_in_list in master_list:
            while ("IN" + str(insurance_no)) in list_in_list:
                insurance_no = int(insurance_no) + 1
        new_insurance_no = "IN" + str(insurance_no)
        print("------------------------------------------------------------------------------")
        return new_insurance_no

    elif choice == "N":
        insurance_no = "no insurance"
        return insurance_no

    else:
        print("Invalid input! Option Y or N only, please try again")
        insurance()


def type_f():
    print("------------------------------------------------------------------------------")
    print("""Please choose the type of ticket you want.\n"""
          """Press [1] - If you want to choose one-way ticket\n"""
          """Press [2] - If you want to choose round-trip ticket""")
    print("------------------------------------------------------------------------------")
    type = input("Choose your type of ticket: ")
    if type == "1":
        print("Successfully, your flight ticket is one-way ticket.")
        ticket = "one-way ticket"
        return ticket

    elif type == "2":
        print("Successfully, your flight ticket is round-trip ticket.")
        ticket = "round-trip ticket"
        return ticket

    else:
        print("Invalid data! Option 1 - 3, please try again")
        type_f()


def class_f():
    print("------------------------------------------------------------------------------")
    print(""""Which class you want to book?\n"""
          """Press [1] - First class\n"""
          """Press [2] - Business class\n"""
          """Press [3] - Economy class""")
    print("------------------------------------------------------------------------------")
    a = input("Choose your class: ")
    if a == "1":
        print("Successfully, your flight is First Class")
        fclass = "First Class"
        return fclass

    elif a == "2":
        print("Successfully, your flight is Business Class")
        fclass = "Business Class"
        return fclass

    elif a == "3":
        print("Successfully, your flight is Economy Class")
        fclass = "Economy Class"
        return fclass

    else:
        print("Invalid data! Option 1 - 3, please try again")
        class_f()


def adult():
    print("------------------------------------------------------------------------------")
    print("""How many ticket you would like to buy?\n"""
          """There are 2 types of ticket.\n"""
          """Adult - 18 years old and above, Children - Below 18 years old.""")
    print("------------------------------------------------------------------------------")
    adult_t = input("Do you need adult ticket?(Y/N): ")
    if adult_t.upper() == "Y":
        adult_ticket = int(input("How many adult ticket you want?: "))
        num_adult = str(adult_ticket)
        return num_adult

    elif adult_t.upper() == "N":
        num_adult = "0"
        return num_adult

    else:
        print("Invalid data! Option Y or N, please try again")
        adult()


def child():
    child_t = input("Do you need child ticket?(Y/N): ")
    if child_t.upper() == "Y":
        child_ticket = int(input("How many child ticket you want?: "))
        num_child = str(child_ticket)
        return num_child
    elif child_t.upper() == "N":
        num_child = "0"
        return num_child
    else:
        print("Invalid data! Option Y or N, please try again")
        child()


def baggage():
    print("------------------------------------------------------------------------------")
    print("""Press[Y] - Checked baggage\n"""
          """Press[N] - Cabin baggage""")
    print("------------------------------------------------------------------------------")
    choice = input("Do you need checked baggage?: ").upper()
    if choice == "Y":
        print("Successfully, you choose Checked baggage.")
        baggage_choice = "Checked baggage"
        return baggage_choice

    elif choice == "N":
        print("Successfully, you choose Cabin baggage.")
        baggage_choice = "Cabin baggage"
        return baggage_choice

    else:
        print("Invalid data! Option Y or N, please try again")
        baggage()


def seat_type():
    print("------------------------------------------------------------------------------")
    print("""Please choose your seat type.\n"""
          """Press [E] - Exit rows seat\n"""
          """Press [A] - Aisle seat\n"""
          """Press [W} - Window seat""")
    print("------------------------------------------------------------------------------")
    seat_t = input("Please enter your seat type: ").upper()
    if seat_t == "E":
        print("Successfully, your seat is exit rows seat.")
        seat = "exit rows seat"
        return seat

    elif seat_t == "A":
        print("Successfully, your seat is aisle seat.")
        seat = "aisle seat"
        return seat

    elif seat_t == "W":
        print("Successfully, your seat is window seat.")
        seat = "window seat"
        return seat

    else:
        print("Invalid data! Option E or A or W, please try again")
        seat_type()


def payment(data_list):
    if data_list[13] == "0" and data_list[14] == "0":
        print("You must buy at least 1 adult or child ticket...")
        no_confirm = "no confirm"
        return no_confirm
    print("+++++++++++++++++++++++++++++++++++++++++++")
    print(f"Flight No              : {data_list[1]}")
    print(f"Departure Airport      : {data_list[2]} - {data_list[3]}")
    print(f"Destination Airport    : {data_list[4]} - {data_list[5]}")
    print(f"Departure Date and time: {data_list[6]} {data_list[7]}")
    if data_list[11] == "round-trip ticket":
        print(f"Return Date and Time   : {data_list[8]} - {data_list[9]}")
    print(f"Ticket type            : {data_list[11]}")
    print(f"Adult Ticket           : {data_list[13]}")
    print(f"Child Ticket           : {data_list[14]}")
    print(f"Flight Class           : {data_list[12]}")
    print(f"Seat Type              : {data_list[16]}")
    print(f"Insurance number       : {data_list[17]}")
    print(f"Total payment          : {data_list[18]}")
    print("+++++++++++++++++++++++++++++++++++++++++++")
    confirm = input("Are you confirm to book the flight?(Y/N): ")
    if confirm.upper() == "Y":
        print("------------------------------------------------------------------------------")
        print("Proceed to payment......")
        print("""Please choose your payment method.\n"""
              """[1] Credit Card\n"""
              """[2] Online transaction\n""")
        payment_method = input("Which payment method you want to use?: ")
        if payment_method == "1":
            card_no = int(input("Please enter your credit card number: "))
            cvc = int(input("Please insert your cvc number: "))
            print("Successfully, your payment has completed.")
            invoice_no = "1000"
            with open("booking.txt", "r") as booked:
                readbooked = booked.read()
                booking_list = readbooked.splitlines()
            master_list = []
            for data in booking_list:
                bookingdata = data.split(",")
                master_list.append(bookingdata)

            for list_in_list in master_list:
                while ("IID" + str(invoice_no)) in list_in_list:
                    invoice_no = int(invoice_no) + 1
            new_invoice_no = "IID" + str(invoice_no)
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Congratulations on completing your booking, your invoice ID is ", new_invoice_no)
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            return new_invoice_no

        elif payment_method == "2":
            receipt_no = input("Please enter online transaction receipt: ")
            print("Successfully, your payment has completed.")
            invoice_no = "1000"
            with open("booking.txt", "r") as booked:
                readbooked = booked.read()
                booking_list = readbooked.splitlines()
            master_list = []
            for data in booking_list:
                bookingdata = data.split(",")
                master_list.append(bookingdata)

            for list_in_list in master_list:
                while ("IID" + str(invoice_no)) in list_in_list:
                    invoice_no = int(invoice_no) + 1
                    invoice_no = str(invoice_no)
            new_invoice_no = "IID" + str(invoice_no)
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Congratulations on completing your booking, your invoice ID is ", new_invoice_no)
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            return new_invoice_no
        else:
            print("Invalid data! Option [1] or [2], please try again")
            payment(data_list)

    elif confirm.upper() == "N":
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Your booking process is cancelled!")
        print("+++++++++++++++++++++++++++++++++++++++")
        no_confirm = "no confirm"
        return no_confirm
    else:
        print("wrong input!You can only enter 'Y' or 'N'")
        payment(data_list)


def total_amount(data_list):
    total_price = 0
    total_price += int(data_list[10])
    if data_list[17] != "no insurance":
        total_price += 200
    else:
        total_price += 0
    for list_in_list in data_list:
        if "one-way ticket" in list_in_list:
            total_price += 200
        elif "round-trip ticket" in list_in_list:
            total_price += 350
        elif "First Class" in list_in_list:
            total_price += 800
        elif "Business Class" in list_in_list:
            total_price += 550
        elif "Economy Class" in list_in_list:
            total_price += 350
        elif "exit rows seat" in list_in_list:
            total_price += 200
        elif "aisle seat" in list_in_list:
            total_price += 300
        elif "window seat" in list_in_list:
            total_price += 350
        elif "Checked baggage" in list_in_list:
            total_price += 200
        elif "Cabin baggage" in list_in_list:
            total_price += 0
        else:
            total_price += 0
    calculate_price = total_price
    adult_child_list = []
    no_adult = int(data_list[13])
    calculate_price_adult = (calculate_price + 20) * no_adult
    adult_child_list.append(calculate_price_adult)
    no_child = int(data_list[14])
    calculate_price_child = (calculate_price + 5) * no_child
    adult_child_list.append(calculate_price_child)
    final_price = int(adult_child_list[0]) + int(adult_child_list[1])
    new_final_price = "RM" + str(final_price)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Your total payment is ", new_final_price)
    print("+++++++++++++++++++++++++++++++++++++++")
    return str(new_final_price)


def member_menu():
    print("""Please choose your option\n"""
          """[1] Open profile\n"""
          """[2] flight Booking\n"""
          """[3] Modify profile\n"""
          """[4] My Booking\n"""
          """[5] Log out\n""")


def member(display_schedule, acc):
    print("Login successfully, dear member.")
    print(" ")
    member_menu()
    while True:
        a = input("Enter your choice : ")
        if a == '1':
            display_detail(acc)
            member_menu()

        elif a == '2':
            book_flight(display_schedule, acc)
            member_menu()

        elif a == '3':
            modify_detail(acc)
            member_menu()

        elif a == '4':
            my_booking(acc)
            member_menu()

        elif a == '5':
            print("Log out successfully")
            break

        else:
            print("Invalid option !!")
