from os import system

import pyfiglet

font = pyfiglet.Figlet(justify="center", width=60)
restaurant_name = font.renderText("Some Restaurant")
starters_heading = font.renderText("Starters")
salads_heading = font.renderText("Salads")
chicken_heading = font.renderText("Chicken")
desserts_heading = font.renderText("Desserts")
beverages_heading = font.renderText("Beverages")

current_menu = 0
op = int()

menus = ["Starters", "Salads", "Chicken", "Desserts", "Beverages", "Print Bill", "Exit"]

starters_list = {
    "Panneer Pakora": 120,
    "Spicy Guacamole": 180
}
salads_list = {}
chicken_list = {}
desserts_list = {}
beverages_list = {}

items_for_bill = {}


def take_input():
    global op

    op = int(input("Select an option: "))


def main_menu():
    global current_menu, op

    system("cls")
    print(restaurant_name)

    for i in range(len(menus)):
        print(i + 1, menus[i])

    try:
        take_input()
    except TypeError:
        print("Enter a valid value")
        main_menu()

    if op == 7:
        print("Thank you for using the app")
        exit(0)
    elif 1 <= op <= len(menus):
        current_menu = op
    else:
        print("Not a valid value")
        main_menu()


def starters():
    global starters_list, op, current_menu

    print(starters_heading)

    k = 1
    for item, cost in starters_list.items():
        print(k, " ", item, "\t", cost)
        k += 1

    print("0. Main Menu")

    try:
        take_input()
    except TypeError:
        print("Enter a valid value")
        starters()

    if 1 <= op <= len(starters_list):
        selected_starter = list(starters_list.keys())[op - 1]
        selected_price = starters_list[selected_starter]
        while True:
            quantity = input("Enter quantity: ")

            try:
                quantity = int(quantity)
                break
            except TypeError:
                print("Enter a valid value")

        add_to_bill(selected_starter, selected_price, quantity)
    elif op == 0:
        current_menu = 0
    else:
        print("Not a valid value")


def salads():
    global salads_list, op, current_menu

    print(salads_heading)

    k = 1
    for item, cost in salads_list.items():
        print(k, " ", item, "\t", cost)
        k += 1

    print("0. Main Menu")

    try:
        take_input()
    except TypeError:
        print("Enter a valid value")
        salads()

    if 1 <= op <= len(salads_list):
        selected_salad = list(salads_list.keys())[op - 1]
        selected_price = salads_list[selected_salad]
        while True:
            quantity = input("Enter quantity: ")

            try:
                quantity = int(quantity)
                break
            except TypeError:
                print("Enter a valid value")

        add_to_bill(selected_salad, selected_price, quantity)
    elif op == 0:
        current_menu = 0
    else:
        print("Not a valid value")


def chicken():
    global chicken_list, op, current_menu

    print(chicken_heading)

    k = 1
    for item, cost in chicken_list.items():
        print(k, " ", item, "\t", cost)
        k += 1

    print("0. Main Menu")

    try:
        take_input()
    except TypeError:
        print("Enter a valid value")
        salads()

    if 1 <= op <= len(chicken_list):
        selected_chicken = list(chicken_list.keys())[op - 1]
        selected_price = chicken_list[selected_chicken]
        while True:
            quantity = input("Enter quantity: ")

            try:
                quantity = int(quantity)
                break
            except TypeError:
                print("Enter a valid value")

        add_to_bill(selected_chicken, selected_price, quantity)
    elif op == 0:
        current_menu = 0
    else:
        print("Not a valid value")


def desserts():
    global desserts_list, op, current_menu

    print(desserts_heading)

    k = 1
    for item, cost in desserts_list.items():
        print(k, " ", item, "\t", cost)
        k += 1

    print("0. Main Menu")

    try:
        take_input()
    except TypeError:
        print("Enter a valid value")
        salads()

    if 1 <= op <= len(desserts_list):
        selected_dessert = list(desserts_list.keys())[op - 1]
        selected_price = desserts_list[selected_dessert]
        while True:
            quantity = input("Enter quantity: ")

            try:
                quantity = int(quantity)
                break
            except TypeError:
                print("Enter a valid value")

        add_to_bill(selected_dessert, selected_price, quantity)
    elif op == 0:
        current_menu = 0
    else:
        print("Not a valid value")


def beverages():
    global beverages_list, op, current_menu

    print(beverages_heading)

    k = 1
    for item, cost in beverages_list.items():
        print(k, " ", item, "\t", cost)
        k += 1

    print("0. Main Menu")

    try:
        take_input()
    except TypeError:
        print("Enter a valid value")
        salads()

    if 1 <= op <= len(beverages_list):
        selected_beverage = list(beverages_list.keys())[op - 1]
        selected_price = beverages_list[selected_beverage]
        while True:
            quantity = input("Enter quantity: ")

            try:
                quantity = int(quantity)
                break
            except TypeError:
                print("Enter a valid value")

        add_to_bill(selected_beverage, selected_price, quantity)
    elif op == 0:
        current_menu = 0
    else:
        print("Not a valid value")


def print_bill():
    global items_for_bill

    print(items_for_bill)

    print("Thank you for visiting")
    exit(0)


def menu_organizer():
    global current_menu

    match current_menu:
        case 0:
            main_menu()
        case 1:
            starters()
        case 2:
            salads()
        case 3:
            chicken()
        case 4:
            desserts()
        case 5:
            beverages()
        case 6:
            print_bill()


def add_to_bill(item, cost, quantity):
    global items_for_bill

    items_for_bill[item] = {
        cost,
        quantity
    }


def main():
    while True:
        menu_organizer()


main()
