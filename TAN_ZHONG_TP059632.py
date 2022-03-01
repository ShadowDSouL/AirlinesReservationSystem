# TAN ZHONG
# TP059632

def admin_option():
    print("""------ Admin Option ------\n"""
          """Press [1] - Add a flight\n"""
          """Press [2] - Modify a flight\n"""
          """Press [3] - Display all records\n"""
          """Press [4] - Logout\n"""
          """--------------------------""")


def admin(display_schedule):
    while True:  # Loop forever for keep getting input from user until Admin Logout
        admin_option()  # Show Admin option
        admin_choice = input("Enter your choice (Option 1 - 4): ")              # Get user choice from the option
        if admin_choice == "1":                                                   # Press "1" to add flight
            add_flight()                                                        # Call function to add flight

        elif admin_choice == "2":                                                 # Press "2" to modify/delete a flight
            display_schedule()                                                           # To show the current schedule
            modify_flight()                                                     # Call function to modify
            display_schedule()                                                           # To show the latest schedule

        elif admin_choice == "3":                                                 # Press "3" to display some records
            while True:
                display_record()
                display_choice = input("Enter your choice (Option 1 - 4): ")
                if display_choice == "1":
                    record_1()
                elif display_choice == "2":
                    record_2()
                elif display_choice == "3":
                    record_3()
                elif display_choice == "4":                                        # Back to admin option
                    break
                else:
                    print("Incorrect option!\n"
                          "Please try again \n")

        elif admin_choice == "4":                                                   # Press "4" to logout
            print("Good bye Admin \(TnT)/ \n"
                  "Logout successfully.\n")
            break                                                                 # Break the loop

        else:                                                                   # To ensure user choose the right option
            print("Incorrect option!\n"
                  "Please try again \n")


def add_flight():
    while True:
        confirmation = input("Press 'any key' to continue\n"
                             "Press [1] to quit add flight function.\n"
                             "Do you wish to continue to add flight?: ")
        if confirmation == "1":                                              # Quit this function when only user press 1
            break
        else:
            flight_list = []
            flight_no = input("\nEnter the flight number: ").upper()
            from_country = input("Enter a country (Departure): ").upper()
            from_city = input("Enter a city (Departure): ").upper()
            to_country = input("Enter the country (Destination): ").upper()
            to_city = input("Enter a city (Destination): ").upper()
            date_d = input("Enter a departure date: ").upper()
            time_d = input("Enter a departure time: ").upper()
            date_r = input("Enter a return date: ").upper()
            time_r = input("Enter a return time: ").upper()
            price = input("Enter a price: RM ").upper()
            if len(flight_no) == 6 and flight_no[0:3] == "AMG":             # Flight number must be 6 characters
                if from_country != "" and from_city != "":                  # These data all cannot be emptied
                    if to_country != "" and to_city != "":
                        if len(date_d) == 6 and len(time_d) == 7:
                            if len(date_r) == 6 and len(time_r) == 7:
                                if price != "":
                                    # When all condition are met, only can add the flight into the txt file
                                    flight_list.append(flight_no)
                                    flight_list.append(from_country)
                                    flight_list.append(from_city)
                                    flight_list.append(to_country)
                                    flight_list.append(to_city)
                                    flight_list.append(date_d)
                                    flight_list.append(time_d)
                                    flight_list.append(date_r)
                                    flight_list.append(time_r)
                                    flight_list.append(price)
                                    print(f"The data has been added into flight list: \n {flight_list}")

                                    with open("airline.txt", "a") as schedule:
                                        for data in flight_list:
                                            if data == flight_list[-1]:
                                                schedule.write(data)
                                            else:
                                                schedule.write(data + ",")
                                        schedule.write("\n")

                                    print("The new flight has been added into the schedule.\n")
                                    break
                                else:
                                    print("The price cannot be emptied! Please try again \n")
                            else:
                                print("""The "format" for return date and time is incorrect!""")
                                print("""The format for date: NOV 11 and time:10.00AM. Please try again \n""")
                        else:
                            print("""The "format" for departure date and time is incorrect!""")
                            print("""The format for date: NOV 11 and time:10.00AM. Please try again \n""")
                    else:
                        print("The destination cannot be emptied! Please try again \n")
                else:
                    print("The departure cannot be emptied! Please try again \n")
            else:
                print("Incorrect data for the flight! Please try again \n")


def modify_data():
    with open("airline.txt", "r") as schedule:
        flight = schedule.read()
        airline = flight.splitlines()

    new_master_airline = []
    for element in airline:
        newAirline = element.split(",")
        new_master_airline.append(newAirline)

    count = 0
    flight_no = input("Enter a flight no: ").upper()
    print("+++++++++++++++++++++++++++++++++++++++")
    for list_in_list in new_master_airline:
        if list_in_list[0] == flight_no:
            print(f"Flight No              : {list_in_list[0]}")
            print(f"Departure Airport      : {list_in_list[1]} - {list_in_list[2]}")
            print(f"Destination Airport    : {list_in_list[3]} - {list_in_list[4]}")
            print(f"Departure Date and time: {list_in_list[5]} {list_in_list[6]}")
            print(f"Return Date and Time   : {list_in_list[7]} {list_in_list[8]}")
            print(f"Price                  : RM{list_in_list[9]}")
            print("+++++++++++++++++++++++++++++++++++++++")
            count += 1

    if count == 0:
        print("               NO RECORD")
        print("+++++++++++++++++++++++++++++++++++++++")
        print("\n")

    if count >= 1:
        country_from = input("Enter a country (Departure): ").upper()
        country_to = input("Enter a country (Destination): ").upper()
        for list_in_list in new_master_airline:
            if list_in_list[0] == flight_no:
                if list_in_list[1] == country_from and list_in_list[3] == country_to:
                    while True:
                        print("To modify which data: \n"
                              "Press [1]  - Flight No \n"
                              "Press [2]  - Country (Departure)\n"
                              "Press [3]  - City (Departure)\n"
                              "Press [4]  - Country (Destination)\n"
                              "Press [5]  - City (Destination)\n"
                              "Press [6]  - Date (Departure)\n"
                              "Press [7]  - Time (Departure)\n"
                              "Press [8]  - Date (Return)\n"
                              "Press [9]  - Time (Return)\n"
                              "Press [10] - Price\n")
                        choice = input("Enter your choice (Option 1 - 10): ")
                        if choice == "1":
                            while True:
                                newData = input("Enter a new data for it (i.e. AMG007): ").upper()
                                if len(newData) == 6 and newData[0:3] == "AMG":
                                    break
                                else:
                                    print("Incorrect format for Flight No! Please try again.")
                            break

                        elif choice == "2" or choice == "3" or choice == "4" or choice == "5":
                            while True:
                                newData = input("Enter a new data for it (i.e. MALAYSIA): ").upper()
                                if newData != "":
                                    break
                                else:
                                    print("This data cannot be emptied! Please try again.")
                            break

                        elif choice == "6" or choice == "8":
                            while True:
                                newData = input("Enter a new data for it (i.e. NOV 10): ").upper()
                                if len(newData) == 6:
                                    break
                                else:
                                    print("""The "format" for date is incorrect!\n""")
                                    print("""The format for date: NOV 11. Please try again \n""")
                            break

                        elif choice == "7" or choice == "9":
                            while True:
                                newData = input("Enter a new data for it (i.e 10.00AM): ").upper()
                                if len(newData) == 7:
                                    break
                                else:
                                    print("""The "format" for time is incorrect!\n""")
                                    print("""The format for time: 10.00AM. Please try again \n""")
                            break

                        elif choice == "10":
                            while True:
                                newData = input("Enter a new data for it (i.e. 5000): ").upper()
                                if newData != "":
                                    break
                                else:
                                    print("This data cannot be emptied! Please try again.")
                            break

                        else:
                            print("Invalid input! (Option 1 - 10)")
                            print("Please try again.")

                    list_in_list[int(choice) - 1] = newData
                    print("The data has been modified.")
                    print(f"New data:{list_in_list}")
                    print("+++++++++++++++++++++++++++++++++++++++")
                    print(f"Flight No              : {list_in_list[0]}")
                    print(f"Departure Airport      : {list_in_list[1]} - {list_in_list[2]}")
                    print(f"Destination Airport    : {list_in_list[3]} - {list_in_list[4]}")
                    print(f"Departure Date and time: {list_in_list[5]} {list_in_list[6]}")
                    print(f"Return Date and Time   : {list_in_list[7]} {list_in_list[8]}")
                    print(f"Price                  : RM{list_in_list[9]}")
                    print("+++++++++++++++++++++++++++++++++++++++")

        with open("airline.txt", "w") as schedule:
            for row in new_master_airline:
                for data in row:
                    if data in row[-1]:
                        schedule.write(data)
                    else:
                        schedule.write(data + ",")
                schedule.write("\n")


def delete_flight():
    # First, choose a departure country or a destination country
    # Then, the flight will be shown according to your country selection
    # Next, choose the flight from the scheduling shown, for delete the particular flight
    # The confirmation will show user which flight will be deleted from the schedule and txt file
    # The delete here is actually rewrite a new txt file all again without the flight that user wish to delete
    # Except the chosen flight, all other flight will be copied back to the new txt file
    with open("airline.txt", "r") as schedule:
        schedule_list = schedule.readlines()
        flight_no = input("Enter a flight no: ").upper()
        print(" " * 90, "Departure", " " * 15, "Return")
        print("Flight number :", " " * 14, "From", " " * 33, "To", " " * 15, "Date     Time(GMT+8)", " " * 3,
              "Date     Time(GMT+8)", "     Price")
        print("-" * 150)
        count = 0
        for line in schedule_list:
            line = line.rstrip()                               # To remove all whitespace at the right side of the line
            line = line.split(",") # returns a list of the words in the string, using "," as the delimiter string.
            num1 = len(line[1])                                # Word count for the schedule display
            num2 = len(line[2])
            num3 = len(line[3])
            num4 = len(line[4])
            space1 = 16 - num1
            space2 = 16 - num2
            space3 = 16 - num3
            space4 = 16 - num4
            if flight_no == line [0]:
                print(" " * 3 + line[0] + "     : " + (" " * space1) + line[1] + " - " + line[2] + (" " * space2)
                      + "->" + (" " * space3) + line[3] + " - " + line[4] + (" " * space4) + line[5] + "    " + line[6]
                      + "    |   " + line[7] + "    " + line[8] + "         RM " + line[9])
                count += 1   # When the desired country is exist in the schedule, it will count the number +1

        if count == 0 :      # The number is 0 when the desired country is not exist in the schedule
            print("                                                                Flight not found!")

        if count >= 1:       # This means the country is found, then only can search the flight number for deleting the flight
            country_from = input("Enter a country (Departure): ").upper()
            country_to = input("Enter a country (Destination): ").upper()
            exist = 0
            for line in schedule_list:
                line = line.rstrip()
                line = line.split(",")
                if flight_no == line[0]:
                    if country_from == line[1] and country_to == line[3]:
                        exist += 1
                        print(f"\nAre you sure you want to delete this flight?\n  "
                              f"{line[0]} : {line[1]} -> {line[3]}")
                        confirmation = input(""""Y" for Yes, "N" for No: """).upper()
                        if confirmation == "Y":
                            with open("airline.txt", "w") as schedule:
                                for line in schedule_list:
                                    if flight_no and country_from and country_to not in line.strip("\n"):
                                        schedule.write(line)
                            print(f"The flight {flight_no} has been delete from the airline schedule.")
                        elif confirmation == "N":
                            print("The modification is cancelled.")
                        else:                                          # To ensure user only put in Y or N
                            print("Invalid input! Your process has been cancelled!")
            if exist == 0:
                print(" " * 90, "Departure", " " * 15, "Return")
                print("Flight number :", " " * 14, "From", " " * 33, "To", " " * 15, "Date     Time(GMT+8)", " " * 3,
                      "Date     Time(GMT+8)", "     Price")
                print("-" * 150)
                print("                                                                Country not found!")



def modify_flight():
    while True:
        modify_choice = input("-------- Modify Option --------\n"
                                  "Press [1] - to modify data\n"
                                  "Press [2] - to delete the flight\n"
                                  "Press [3] - go back\n"
                                  "Enter your choice (1 or 3): ")
        if modify_choice == "1":
            modify_data()
            break
        elif modify_choice == "2":
            delete_flight()
            break
        elif modify_choice == "3":
            break
        else:
            print("Incorrect input! Option (1 -3), please try again!")


def display_record():
    print("""------------ Display Record -----------\n"""
          """Press [1] - flight schedule by flight numbers\n"""
          """Press [2] - flight booked by customer\n"""
          """Press [3] - total ticket sold\n"""
          """Press [4] - Back to "Admin Option"\n"""
          """----------------------------------------""")


def record_1():
    # This function is to display a particular flight schedule
    # First, put in the flight no for searching
    # Next, open file and read file
    # Then, split and put line by line into a list
    # Then, for loop in list, take the first element in the list
    # Then, take split those elements with ",", the index is there now, i.e index 0, index 1, index 2, and so on
    # Finally, when the input(flight no) == element [0]
    # Print those data where met the condition
    flight_number = input("Enter a Flight No to search the flight (i.e. AMG009): ").upper()
    count = 0
    with open("airline.txt", "r") as schedule:
        flights = schedule.read()
        content_listByLine = flights.splitlines()

    print("+++++++++++++++++++++++++++++++++++++++")
    for data in content_listByLine:
        data = data.split(",")
        if data[0] == flight_number:
            print(f"Flight No              : {data[0]}")
            print(f"Departure Airport      : {data[1]} - {data[2]}")
            print(f"Destination Airport    : {data[3]} - {data[4]}")
            print(f"Departure Date and time: {data[5]} {data[6]}")
            print(f"Return Date and Time   : {data[7]} {data[8]}")
            print(f"Price                  : RM{data[9]}")
            print("+++++++++++++++++++++++++++++++++++++++")
            count += 1
    if count == 0:
        print("               NO RECORD")
        print("+++++++++++++++++++++++++++++++++++++++")
    print("\n")


def record_2():
    with open("booking.txt", "r") as transaction:
        record = transaction.read()
        booking_list = record.splitlines()
    master_list = []

    for data in booking_list:
        bookingdata = data.split(",")
        master_list.append(bookingdata)

    print("--------------------------------------------------------------------")
    for list_in_list in master_list:
        print(f"Flight no: {list_in_list[1]}:")
        print(f"From: {list_in_list[2]} To: {list_in_list[4]} | {list_in_list[6]} {list_in_list[7]}")
        print(f"Booked by: {list_in_list[0]}")
        print("--------------------------------------------------------------------")


def record_3():
    # This function is used to display the ticket sold and profit
    while True:
        print("----------- Ticket Sold or Profit Earned -----------\n"
              "Press [1] - Display profit for the particular transaction\n"
              "Press [2] - Display total ticket sold and profit earned\n"
              "Press [3] - Back to Display Record Menu\n"
              "-----------------------------------------------------")
        choice = input("Enter your choice (Option 1 - 3): ")
        if choice == "1":
            # Give invoice no as input to search for the transaction in the txt file
            # Open and read file
            # split and put line by line into the list
            # For loop in list, take the element in the list
            # Split those element with ":", then the index appear
            # When the input(invoice number) == data[0]
            # Print those data
            invoice_no = input("Enter the invoice number (i.e IID1001): ")
            count = 0
            with open("booking.txt", "r") as transaction:
                record = transaction.read()
                content_listByLine = record.splitlines()
            print("+++++++++++++++++++++++++++++++++++++++")
            for data in content_listByLine:
                data = data.split(",")
                # profit 16, invoice 17, ticket sold 11,12
                if data[-1] == invoice_no:
                    tickets_sold = int(data[13]) + int(data[14])
                    print(f"Invoice number : {data[-1]}")
                    print(f"Ticket Sold    : {tickets_sold}")
                    print(f"Profit earned  : {data[-2]}")
                    print("+++++++++++++++++++++++++++++++++++++++\n")
                    count += 1 # This count means the number of data found
            if count == 0 :    # The number of data found is 0 = no data
                print("The invoice number is not existed in the tickets_profit.txt \n")

        elif choice == "2":
            # Set total ticket sold = 0
            # Set profit = 0
            # Open and read file
            # Split and put line by line in to a list
            # For loop, take element in list and split it with ":"
            # total ticket sold is in the index 1
            # profit is in the index 2
            # add them together and display it
            total_ticket_sold = 0
            total_profit = 0
            no_of_transaction = 0
            with open("booking.txt", "r") as transaction:
                record = transaction.read()
                content_listByLine = record.splitlines()

            for data in content_listByLine:
                no_of_transaction += 1
                data = data.split(",")
                total_ticket_sold += int(data[13]) + int(data[14])
                profit = data[-2]
                total_profit += int(profit[2:])
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f"The total number of transactions     : {no_of_transaction}")
            print(f"The total ticket sold                : {total_ticket_sold}")
            print(f"The total profit earned (Up to date) : RM{total_profit}")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

        elif choice == "3":
            # back to the previous page
            break
        else:
            # To ensure user give corrects input
            print("Invalid input! Please try again!\n")
