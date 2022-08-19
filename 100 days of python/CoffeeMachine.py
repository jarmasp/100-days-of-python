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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def payment():

    print ('please insert coins: ')

    quarters = input('how many quarters?: ')
    dimes = input('how many dimes?: ')
    nickles = input('how many nickles?: ')
    pennies = input('how many pennies?: ')

    if quarters == '':
        quarters = 0
    if dimes == '':
        dimes = 0
    if nickles == '':
        nickles = 0
    if pennies == '':
        pennies = 0

    total = (int(quarters) * 0.25) + (int(dimes) * 0.10) + (int(nickles) * 0.05) + (int(pennies) * 0.01)

    return total
    
def check_resources(drink):
    for item in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][item] > resources[item]:
            print (f'Sorry there is not enough {item}')
            return False
    return True

def make_coffee(drink, money):
    for item in MENU[drink]['ingredients']:
        resources[item] -= MENU[drink]['ingredients'][item]
    print (f'Here is ${money} in change')
    print (f'Here is your {drink} ☕️ Enjoy!')

def coffee_machine():
    global money
    command = input('What would you like? (espresso/latte/cappuccino): ')
    if command == 'espresso' or command == 'latte' or command == 'cappuccino':
        if check_resources(command):
            total = payment()
            if total >= MENU[command]['cost']:
                make_coffee(command, total - MENU[command]['cost'])
                money += MENU[command]['cost']
            else:
                print ('Sorry that\'s not enough money. Money refunded.')
        coffee_machine()
    elif command == 'report':
        print (resources)
        print (money)
        coffee_machine()
    elif command == 'off':
        print (resources)
        print (money)
        exit()
    else:
        print ('Invalid command')
        coffee_machine()

coffee_machine()