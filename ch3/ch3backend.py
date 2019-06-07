"""
cd Desktop/workspace/PythonBusinessChallenges
git remote add (could be anything) but we are using) origin html-link
get remote -v (when you pull it will come from, when you push it will go to)
Here's what they'd like:
1. Display a list of all outings.
2. Add individual outings to a list(don't need to worry about delete yet)
3. Calculations:
	They'd like to see a display for the combined cost for all outings.
	They'd like to see a display of outing costs by type.
		For example, all bowling outings for the year were $2000.00.
		All Concert outings cost $5000.00.
"""





class Outing:
    def __init__(self, outing_date, outing_type, cost_of_outing, number_of_attendents):
        self.outing_date = outing_date
        self.outing_type = outing_type
        self.cost_of_outing = cost_of_outing
        self.num_attend = number_of_attendents

    def __repr__(self):
        return f"'outing date: '{self.outing_date} \t 'outing type: '{self.outing_type} \t 'outing cost: $'{self.cost_of_outing} \t 'number of people that attended: '{self.num_attend} \n "


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

    def show_all_cost_by_type(self, event, cost):
        if event == "golf":
            self.golf_operator = self.golf_operator + cost

        elif event == "bowling":
            self.bowling_operator = self.bowling_operator + cost

        elif event == "amusement park":
            self.amusement_operator = self.amusement_operator + cost

        elif event == "concert":
            self.concert_operator = self.concert_operator + cost

        else:
            pass


############################### ignore all lines of code after this
"""
total_operator = 0

for i in event_list:
    if i[1] == x:
        total += 1[0]
#i.eventtype = cost
print(total)
"""



"""
    def remove_menu_item(self, yeet):
        for i in self.menulist:
            if i.meal_num == yeet:
                self.menulist.remove(i)
                return True
        return False
"""