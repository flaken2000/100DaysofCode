from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

# Main code
machine_on = True
while machine_on:
    machine_action = input(f"What would you like? ({menu.get_items()}): ")
    if machine_action == "report":
        coffee_maker.report()
        money_machine.report()
    elif machine_action == "off":
        machine_on = False
    elif machine_action == "espresso" or machine_action == "latte" or machine_action == "cappuccino":
        # Drink ordered
        # Create MenuItem object
        drink = menu.find_drink(machine_action)
        # Check if sufficient resources
        if coffee_maker.is_resource_sufficient(drink):
            print(f"{drink.name} is ${drink.cost}")
            if money_machine.make_payment(drink.cost):
                # Enough money, making drink
                coffee_maker.make_coffee(drink)


