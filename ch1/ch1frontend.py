

from ch1frontend import Menu_item, Usrmenu

# user can add, remove, and print menu, can exit
my_menu = Usrmenu()

while True:
    print(  "Menu Manager\n"
            "1. print menu\n"
            "2. add to menu\n"
            "3. remove from menu\n"
            "4. exit"
    )

    usr_choice = input("> ")
    if usr_choice == "1":
        food_menu = my_menu.get_menu()
        for food in food_menu:
            print(food)
    elif usr_choice == "2":
        food_name = input("name: >")
        food_desc = input("description: >")
        food_ingredi = input("indrients: >")
        food_cost = input("cost: >")
        my_menu.add_item(food_name, food_desc, food_ingredi, food_cost)
        print("successfully added item to menu")
    elif usr_choice == "3":
        deleet = int(input("what menu number are we removing? >"))
        my_menu.remove_menu_item(deleet)
    elif usr_choice == "4":
        exit()
    else:
        print("invalid input")

























"""
my_menu = Usrmenu()

my_menu_list = my_menu.get_menu()
print(my_menu_list)

Usrmenu.add_item("eggs", "these are eggs", ["eggs"], 1.00)
print(my_menu_list)

print(item)

my_meu.remove_menu_item(1)
print(my_menu_list)
"""