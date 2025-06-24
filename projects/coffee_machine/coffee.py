MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}
resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
def check_resources(drink):
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coins():
    return int(input("quarters: ")) * 0.25 + int(input("dimes: ")) * 0.10 + int(input("nickels: ")) * 0.05 + int(input("pennies: ")) * 0.01
def make_coffee(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    resources["money"] += MENU[drink]["cost"]
    print(f"Here is your {drink} ☕️")
def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            break
        elif choice == "report":
            for item in resources:
                print(f"{item}: {resources[item]}")
        elif choice in MENU:
            if check_resources(choice):
                payment = process_coins()
                if payment >= MENU[choice]["cost"]:
                    change = round(payment - MENU[choice]["cost"], 2)
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    make_coffee(choice)
                else:
                    print("Sorry that's not enough money.")
coffee_machine()