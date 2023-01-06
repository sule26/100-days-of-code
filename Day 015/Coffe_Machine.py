from data import MENU, profit, resources, coins


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry, there is not enough {item}')
            return False
    return True


def process_coins(coins):
    total = 0
    for coin_name, coin_value in coins.items():
        total += int(input(f"How many {coin_name}? ")) * coin_value
    return total


def coffee_machine():
    is_on = True
    while is_on:
        global profit
        order = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        if order == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        elif order == "off":
            is_on = False
            print("Coffee machine turned off!")
        else:
            if check_resources(MENU[order]['ingredients']):
                total = process_coins(coins)
                if total > MENU[order]['cost']:
                    change = total - MENU[order]['cost']
                    profit += MENU[order]['cost']
                    make_coffee(order, MENU[order]['ingredients'])
                    print(f"Here is ${change:.2f} change!")
                else:
                    print("Sorry, not enough money!")


coffee_machine()
