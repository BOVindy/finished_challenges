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