from menu import Menu
from menu_item import MenuItem
from character import *
import json
import os


def new_game():
    user_name = input("Please enter your name: ")
    user.name = user_name
    print("Your character name is " + user_name + ".")
    new_game_submenu.display_menu()

def load_game():
    print("saved games:")
    list_json_files()

# def load():
#     saved_games = []
#     input_file = open(saved_game_list + ".json", "r")
#     try:
#         saved_games = json.load(input_file)
#     except Exception:
#         pass
#     input_file.close()
#     return saved_games

def exit_game():
    exit()

def continue_newgame():
    user.random_status()
    user.print_roll_status()
    continue_submenu.display_menu()

def list_json_files():
    json_list = []
    for file in os.listdir():
        if file.endswith(".json"):
            json_list.append(file)
    for item in json_list:
        print(item.split('.')[0])
    return json_list

def ultimate_save():
    save_submenu.display_menu()

def save():
    print("already saved items: ")
    list_json_files()
    print()
    save_submenu.display_menu()

def show_quit_submenu():
    quit_submenu.display_menu()

def save_and_quit():
    json_file_name = input("Please enter a file name: ")
    output_file = open(json_file_name + '.json', 'w')
    json.dump(user.create_dictionary(), output_file)
    output_file.close()
    print("Your game is saved.")
    exit()

def save_rewrite_and_quit():
    print("already saved items: ")
    list_json_files()
    print()
    json_file_name = input("Please enter a file name from the list: ")
    output_file = open(json_file_name + '.json', 'w')
    json.dump(user.create_dictionary(), output_file)
    output_file.close()
    print("Your game is saved.")
    exit()

def resume():
    pass

def continue_to_potion():
    print("Please choose a potion: ")
    choose_potion_submenu.display_menu()


def health_potion():
    user.inventory[0] = "Potion of Health"
    print("You have chosen: " + user.inventory[0])
    potion_submenu.display_menu()

def dexterity_potion():
    user.inventory[0] = "Potion of Dexterity"
    print("You have chosen: " + user.inventory[0])
    potion_submenu.display_menu()

def luck_potion():
    user.inventory[0] = "Potion of Luck"
    print("You have chosen: " + user.inventory[0])
    potion_submenu.display_menu()

def continue_begin():
    print("The status of your character:")
    user.print_roll_status()
    user.print_inventory_status()
    begin_submenu.display_menu()

def begin_game():
    print("Test your sword in a test fight!" + "\n")
    monster.name = "opi"
    monster.random_status()
    user.print_start_status_character()
    monster.print_start_status_monster()
    fight_submenu.display_menu()

def retreat():
    print("You cannot retreat")
    begin_submenu.display_menu()

def try_luck():
    pass

def strike():
    if fight.is_hit():
        print("You hit the monster!")
    else:
        print("The monster hit you!")
    after_strike_submenu.display_menu()

def new_strike():
    fight.after_strike()
    fight_submenu.display_menu()

main_menu = Menu([
    MenuItem(1, "New Game", new_game),
    MenuItem(2, "Load Game", load_game),
    MenuItem(3, "Exit", exit_game)
])

new_game_submenu = Menu([
    MenuItem(1, "Reenter name", new_game),
    MenuItem(2, "Continue", continue_newgame),
    MenuItem(3, "Save", ultimate_save),
    MenuItem(4, "Quit", show_quit_submenu),
])



quit_submenu = Menu([
    MenuItem(1, "Save and Quit", ultimate_save),
    MenuItem(2, "Quit without save", exit_game),
    MenuItem(3, "Resume", resume)
])

save_submenu = Menu([
    MenuItem(1, "Add new item", save_and_quit),
    MenuItem(2, "Rewrite a saved item", save_rewrite_and_quit),
    MenuItem(3, "Resume", resume),
    MenuItem(4, "Quit", show_quit_submenu)
])



continue_submenu = Menu([
    MenuItem(1, "Reroll stats", continue_newgame),
    MenuItem(2, "Continue", continue_to_potion),
    MenuItem(3, "Save", save),
    MenuItem(4, "Quit", show_quit_submenu)
])

choose_potion_submenu = Menu([
    MenuItem(1, "Potion of Health", health_potion),
    MenuItem(2, "Potion of Dexterity", dexterity_potion),
    MenuItem(3, "Potion of Luck", luck_potion)
])

potion_submenu = Menu([
    MenuItem(1, "Reselect the Potion", continue_to_potion),
    MenuItem(2, "Continue", continue_begin),
    MenuItem(3, "Quit", show_quit_submenu)
])

begin_submenu = Menu([
    MenuItem(1, "Begin", begin_game),
    MenuItem(2, "Save", save),
    MenuItem(3, "Quit", show_quit_submenu)
])

fight_submenu = Menu([
    MenuItem(1, "Strike", strike),
    MenuItem(2, "Retreat", retreat),
    MenuItem(3, "Quit", show_quit_submenu)
])


after_strike_submenu = Menu([
    MenuItem(1, "Continue", new_strike),
    MenuItem(2, "Try your luck", try_luck),
    MenuItem(3, "Retreat", retreat),
    MenuItem(4, "Quit",show_quit_submenu),
])


main_menu.display_menu()
