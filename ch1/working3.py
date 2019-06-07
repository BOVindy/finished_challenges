
last_id = 0

class MenuItem:
    def __init__(self, meal_name, meal_description, meal_ingredients, meal_price):
        global last_id
        last_id += 1
        self.meal_number = last_id
        self.meal_name = meal_name
        self.meal_description = meal_description
        self.meal_ingredients = meal_ingredients()
        self.meal_price = meal_price


item_name = input(
    "What is the item you want to add the menu? \n> "#,
"""    "\n please enter a description of the menu item: \n> ",
    ["\n what are the ingeredients of your menu item: \n> "],
    "\n What is the price of your menu item? >"
        """
)
item_description = input("\n please enter a description of the menu item: \n> ")
item_ingredients = input(["\n what are the ingeredients of your menu item: \n> "])
item_price = input("\n What is the price of your menu item? >")

new_item = MenuItem(item_name, item_description, item_ingredients, item_price)
"""

item_description = input("\n please enter a description of the menu item: \n> ")
new_item = MenuItem(item_description)

item_ingredients = input(["\n what are the ingeredients of your menu item: \n> "])
new_item = MenuItem(item_ingredients)

item_price = input("\n What is the price of your menu item? >")
new_item = MenuItem(item_price)
"""

"""
        def add_note(self):
            menu.item = self.meal_name




            print(f"{menu.item} has been added to your menu")
        
        message = input("Enter a message: ")
        self.notebook.new_note(message)
        print("your note has been added.")
"""
"""
        def start_car(self, car, age):
        car.driver = self.name
        car.status = "on"
        print(f"{car.driver} has started the car")
"""
"""
usr_item = input("What is the item you want to add the menu? > ")
new_menu_item = MenuItem(usr_item)

description = input("please enter a description of the menu item: ")
new_item_description = MenuItem(description)

# ingredients = input("please enter menu item number: ")
new_item_ingredients = MenuItem(ingredients)

price = input("please enter menu item price: ")
new_item_price = MenuItem(price)

print(new_menu_item.meal_name)

print(new_item_price.meal_price)

"""
"""
    def new_item(self, "number", "name", "description", "ingredients", "price", message):
        self.notes.append(Note(message))
        number = input("please enter menu item number: ")
        name = input("please enter a name for the menu item: ")
        description = input("please enter a description of the menu item: ")
        # ingredients = input("please enter menu item number: ")
        price = input("please enter menu item price: ")
        self.number = number
        self.name = name
        self.description = description
        self.ingredients = ingredients()
        self.price = price

"""