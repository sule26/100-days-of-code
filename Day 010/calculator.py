import os
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

calculation_finished = False


def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculatin with {result}, or 'n' to start a new calculation:  ").lower() == 'y':
            num1 = result
        else:
            should_continue = False
            os.system('cls')
            calculator()


calculator()
