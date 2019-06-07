"""
needs a user menu
    needs options:
        add a badge:
            badge id
            door access
            name?

        update a badge
            change door acces
            change name?

        list all badges
        
        exit

    needs a way to handle errors



needs object badge
    needs:
        badge id:
            needs checks for valid input or invalid input

        list of doors badge has access to:
            potentially a list of doors:
                is door a valid door or not
        
        name of badgeholder?
            check for numbers?
"""
badges = {}

while True:
    print("\n 1 to make a badge \n", "2 to update a badge's door privileges \n", "3 to remove a badge \n", "4 to print all badges \n", "5 exit program \n")
# stretch goal "5/6 to add doors to master list of doors available \n", 
    op = input("> ")

#add badge option
    if op == "1":
        b_id = input("please enter a badge id: ")
        badges.update({b_id: []})
        while True:
            add_door = input("add door privileges to badge? y or n: \n> ").lower()
            if add_door == "y":
                b_door_priv = input("please enter a door that you would like to add to the badge privileges: \n> ")
    #stretch     try valid door
    #stretch     except
                badges[b_id].append(b_door_priv)
                while True:
                    add_another = input("would you like to add another door? y or n \n> ").lower()
                    if add_another == "y":
                        b_door_priv = input("please enter a door that you would like to add to the badge privileges: \n> ")
                        badges[b_id].append(b_door_priv)
                    if add_another == "n":
                        break
                break
            elif add_door == "n":
                break
            else:
                print("you done goofed")

#update option
    elif op == "2":
        b_updater = input("which badge_id would you like to update? ")
        while True:
            if b_updater in badges:
                while True:
                    choice = input("what would you like to do; \n"
                                "1. add a door privilege \n"
                                "2. remove doors from privilege list \n > "
)

                    if choice == "1":
                        b_door_priv = input("please enter a door that you would like to add to the badge privileges: \n> ")
                        badges[b_id].append(b_door_priv)
                    elif choice == "2":
                        b_door_priv = input("please enter a door that you would like to add to the badge privileges: \n> ")
                        try:
                            badges[b_id].remove(b_door_priv)
                        except:
                            print("please choose a valid door to remove")
                    else:
                        print("please choose a valid option. (1 or 2)")
            else:
                print("please enter a valid badge_id")

#remove option
    elif op == "3":
        b_remover = input("which badge_id would you like to remove? ")
        if b_remover in badges.keys():
            badges.pop(b_remover)
        else:
            print("please enter a valid badge_id number")

#print all badges option
    elif op == "4":
        for k, v in badges.items():
            print(f"key: {k} \t \t door access:{v} \n")

    elif op == "5":
        exit()

############################### ignore all lines of code after this, they would only become useful if file was seperated into a frontend and backend... which I didn't have time for
"""
class badge:
    def __init__(self, outing_date, outing_type, cost_of_outing, number_of_attendents):
        badges = {}
        
        self.outing_date = outing_date
        self.outing_type = outing_type
        self.cost_of_outing = cost_of_outing
        self.num_attend = number_of_attendents

    def __repr__(self):
        return f"{self.outing_date} {self.outing_type} ${self.cost_of_outing} #{self.num_attend} \n "


class Usrmenu:
    def __init__(self):
        self.outinglist = []
        self.total_operator = 0.00
        self.golf_operator = 0.00
        self.bowling_operator = 0.00
        self.amusement_operator = 0.00
        self.concert_operator = 0.00

    def show_all_outings(self):
        return self.outinglist

    def add_outing(self, outing_date, outing_type, cost_of_outing, number_of_attendents):
        new_outing = Outing(outing_date, outing_type, cost_of_outing, number_of_attendents)
        self.outinglist.append(new_outing)

    def show_all_total_cost(self):
        for i in self.outinglist:
            self.total_operator += i.cost_of_outing
        return self.total_operator

        return self.outinglist

    def show_all_cost_by_type(self):
        for i in self.outinglist:
            if i.outing_type == "golf":
                self.golf_operator = self.golf_operator + i.cost_of_outing
                return self.golf_operator

            elif i.outing_type == "bowling":
                self.bowling_operator = self.bowling_operator + i.cost_of_outing
                return self.bowling_operator

            elif i.outing_type == "amusement park":
                self.amusement_operator = self.amusement_operator + i.cost_of_outing
                return self.amusement_operator

            elif i.outing_type == "concert":
                self.concert_operator = self.concert_operator + i.cost_of_outing
                return self.concert_operator

            else:
                break

        return self.outinglist
"""