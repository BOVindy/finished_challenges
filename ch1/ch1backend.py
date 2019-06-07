meal_id = 0

class Menu_item:
    def __init__(self, meal_name, description, ingredients, price):
        global meal_id
        meal_id += 1
        self.meal_num = meal_id
        self.meal_name_desired = meal_name
        self.meal_description = description
        self.meal_ingredients = ingredients
        self.meal_price = price

    def __repr__(self):
        return f"#{self.meal_num} {self.meal_name_desired} {self.meal_description} {self.meal_ingredients} ${self.meal_price}"

        #"" ".join(self.ingredients) on a seperate line so ingred = this

class Usrmenu:
    def __init__(self):
        self.menulist = []

    def get_menu(self):
        return self.menulist

    def add_item(self, meal_name, description, ingredients, price):
        new_item = Menu_item(meal_name, description, ingredients, price)
        self.menulist.append(new_item)

    def remove_menu_item(self, yeet):
        for i in self.menulist:
            if i.meal_num == yeet:
                self.menulist.remove(i)
                return True
        return False