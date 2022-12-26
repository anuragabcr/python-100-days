MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def insert_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def order_process(opt, amt):
    global profit
    profit +=  MENU[opt]['cost']
    resources["water"] -= MENU[opt]['ingredients']['water']
    resources["milk"] -= MENU[opt]['ingredients']['milk']
    resources["coffee"] -= MENU[opt]['ingredients']['coffee']
    print(f"Here is yours {opt} and remaining balance {amt-MENU[opt]['cost']}")


def drink(opt):
    order = MENU[opt]
    if resources['water'] < order['ingredients']['water'] or resources['milk'] < order['ingredients']['milk'] or resources['coffee'] < order['ingredients']['coffee']:
        print("Can't process order\nresources not available")
    else:
        amt = insert_coin()
        if amt < order['cost']:
            print("Not enough amount inserted")
        else:
            order_process(opt, amt)


is_on = True
while is_on:
    choice = input("what would you like?(espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink(choice)

