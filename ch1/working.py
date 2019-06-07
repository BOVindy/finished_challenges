"""
The Komodo Cafe is getting a new menu.

The cafe manager at Komodo wants to be able to create a menu item, delete a menu item,
and list all items on the cafe's menu. She needs a console app.

Each of their menu items will contain the following:
a meal number so employees can say "I'll have the #5",
a meal name,
a description,
a list of ingredients in the meal,
and a price.

Your task is to do the following:
1. Create a Menu class with constructors and instance attributes.
2. Create a MenuRepository class that has methods needed.
3. Create a Test Class for your repository methods. (You don't need to test
your constructors or objects. Just the methods.)
4. Create a User Interface file that allows the restaurant manager to add, delete,
and see all items in the menu list.

Notes:
We don't need to update the items right now.
"""

# menu item needs: 
# a meal #
# a meal name
# a description
# a list of ingredients
# a price

import sys
from notebook import Notebook

    def __repr__(self):
        return f"{self.id}|{self.message}"

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.new_item,
            "2": self.list_items,
            "3": self.delete_item,
            "4": exit
        }

    def display_options(self):
        print(
"""
Editor's options:
1. Add new item
2. Show all menu items
3. Delete menu item
4. Exit program
"""
)

    def run(self):
        while True:
            self.display_options()
            choice = input("enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
            for note in notes:
                print(f"{note.id}. {note.message}")

    def add_note(self):
        message = input("Enter a message: ")
        self.notebook.new_note(message)
        print("your note has been added.")

    def update_note(self):
        note_id = input("enter a note id: ")
        message = input("Enter a message: ")
        if message:
            result = self.notebook.update_message(note_id, message)
        if result == False:
            print("Failed to update note.")
        else:
            print("note updated")


if __name__ == "__main__":
    menu = Menu()
    menu.run()


class Notebook:
    def __init__(self):
        self.notes = []

    def new_item(self, "number", "name", "description", "ingredients", "price", message):
        self.notes.append(Note(message))
        self.number = number
        self.name = name
        self.description = description
        self.ingredients = ingredients()
        self.price = price

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def update_message(self, note_id, message):
        note = self._find_note(note_id)
        if note:
            note.message = message
            return True
        return False


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.new_item,
            "2": self.list_items,
            "3": self.delete_item,
            "4": exit
        }

    def display_options(self):
        print(
"""
Editor's options:
1. Add new item
2. Show all menu items
3. Delete menu item
4. Exit program
"""
)

    def run(self):
        while True:
            self.display_menu()
            choice = input("enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

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















    def add_note(self):
        message = input("Enter a message: ")
        self.notebook.new_note(message)
        print("your note has been added.")

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
            for note in notes:
                print(f"{note.id}. {note.message}")



















    def update_note(self):
        note_id = input("enter a note id: ")
        message = input("Enter a message: ")
        if message:
            result = self.notebook.update_message(note_id, message)
        if result == False:
            print("Failed to update note.")
        else:
            print("note updated")

if __name__ == "__main__":
    menu = Menu()
    menu.run()
