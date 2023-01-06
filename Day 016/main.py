from menu import Menu
from money_machine import MoneyMachine
from coffe_maker import CoffeeMaker


def coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    is_on = True
    while is_on:
        order = input(f"\nWhat would you like? ({menu.get_items()}): ")
        if order == "report":
            coffee_maker.report()
            money_machine.report()
        elif order == "off":
            is_on = False
        else:
            drink = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


coffee_machine()
