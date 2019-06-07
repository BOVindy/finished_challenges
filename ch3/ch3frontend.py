
from ch3backend import Outing, Usrmenu

"""
x = int(input("# "))
if x % 4 == 0
    print("cool")
# string.split
"""

my_menu = Usrmenu()

while True:
    print(  "--Outings manager: --\n"
            "1. show all outings\n"
            "2. add an outing\n"
            "3. show total outings cost\n"
            "4. show outings cost by type\n"
            "5. exit"
    )

    usr_choice = input("> ")

    if usr_choice == "1":
        outing_list = my_menu.show_all_outings()
        for outing in outing_list:
            print(outing)

    elif usr_choice == "2":
        while True:
            outing_date = input("what date was/is the outing on? (please enter in day-month-year format including dashes)\n > ")
            try:
                outing_date_list = outing_date.split("-")
                day, month, year = outing_date_list
                day, month, year = int(day), int(month), int(year)
                if year < 2051 and year > 1969:
                    break
                else:
                    print("please enter a valid year")
                    break
                if year % 4 == 0:
                    try:
                        month < 13
                    except:
                        print("please enter a valid month")
                        break

                    if month == "2":
                        try:
                            day < 30
                        except:
                            print("please enter a valid day for February (this is a leap year) ")
                            break
                    if month in ["4", "6", "9", "11"]:
                        try:
                            day < 31
                        except:
                            print("please enter a valid day for this month")
                            break
                    if month in ["1", "3", "5", "7", "8", "10", "12"]:  
                        try:
                            day < 32
                        except:
                            print("please enter a valid day for this month")
                            break
                else:
                    try:
                        month < 13
                    except:
                        print("please enter a valid month")
                        break

                    if month == "2":
                        try:
                            day < 39
                        except:
                            print("please enter a valid day for February (this is not a leap year) ")
                            break
                    if month in ["4", "6", "9", "11"]:
                        try:
                            day < 31
                        except:
                            print("please enter a valid day for this month")
                            break
                    if month in ["1", "3", "5", "7", "8", "10", "12"]:
                        try:
                            day < 32
                        except:
                            print("please enter a valid day for this month")
                            break

            except:
                print("please enter the outing date in day-month-year format, including dashes")
                break


        while True:
            outing_type = input("outing type: (golf, bowling, amusment park, concert)\n > ")
            if outing_type in ["golf", "bowling", "amusement park", "concert"]:
                break
            else:
                print("please enter a valid outing type. ex.(golf, bowling, amusment park, concert)")


        cost_of_outing = input("what was the cost of the event? \n > ")
        try:
            cost_of_outing = int(cost_of_outing)
        except:
            print("please enter a numerical value")
            break


        number_of_attendents = input("how many people attended this outing? \n > ")
        try:
            number_of_attendents = int(number_of_attendents)
        except:
            print("please enter a numerical value")
            break


        my_menu.add_outing(outing_date, outing_type, cost_of_outing, number_of_attendents)
        my_menu.show_all_cost_by_type(outing_type, cost_of_outing)
        print("successfully added outing to the list of outings \n ")

    elif usr_choice == "3":
        print(my_menu.show_all_total_cost())
        print(outing_list)

    elif usr_choice == "4":
        print(my_menu.golf_operator)
        print(my_menu.bowling_operator)
        print(my_menu.amusement_operator)
        print(my_menu.concert_operator)
        print(my_menu.outinglist)

    elif usr_choice == "5":
        exit()
    else:
        print("invalid input")
