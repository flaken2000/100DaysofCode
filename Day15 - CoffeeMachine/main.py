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
    "money": 0
}


def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"coffee: {coffee}g")
    print(f"Money: ${money}")


def check_resources(drink_type):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    for ingredient in MENU[drink_type]["ingredients"]:
        if ingredient == "water":
            water -= MENU[drink_type]["ingredients"]["water"]
        if ingredient == "milk":
            milk -= MENU[drink_type]["ingredients"]["milk"]
        if ingredient == "coffee":
            coffee -= MENU[drink_type]["ingredients"]["coffee"]
    if water < 0 or milk < 0 or coffee < 0:
        if water < 0:
            print("Sorry, there is not enough water")
        elif milk < 0:
            print("Sorry, there is not enough milk")
        elif coffee < 0:
            print("Sorry, there is not enough coffee")
    else:
        new_resources = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
            "money": resources["money"]
             }
        return new_resources


def get_coffee_cost(drink_type):
    return MENU[drink_type]["cost"]


def calculate_money(quarters, dimes, nickels, pennies):
    """Returns total from input"""
    return (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

# Main code
machine_on = True
while machine_on:
    machine_action = input("What would you like? (espresso/latte/cappuccino): ")
    if machine_action == "report":
        print_report()
    elif machine_action == "off":
        machine_on = False
    elif machine_action == "espresso" or machine_action == "latte" or machine_action == "cappuccino":
        new_resources = check_resources(machine_action)
        if new_resources is not None:
            # There is sufficient resources, ask for coins
            coffee_cost = get_coffee_cost(machine_action)
            print(f"{machine_action} is ${coffee_cost}")
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            money = calculate_money(quarters, dimes, nickels, pennies)
            print(f"Money inserted: ${money}")
            if money >= coffee_cost:
                # Make coffee, deduct resources and add money
                print(f"Here is your delicious {machine_action}. Enjoy!")
                new_resources["money"] += coffee_cost
                resources = new_resources
                if money > coffee_cost:
                    # Offer change
                    change = round(money - coffee_cost, 2)
                    print(f"Here is ${change} dollars in change.")

            else:
                print("Sorry, that's not enough money. Money refunded.")
