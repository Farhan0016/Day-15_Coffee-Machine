# from machine_data import MENU, resources
#
#
# def is_resources(coffee_name):
#     recipe = MENU[coffee_name]['ingredients']
#     if recipe['water'] <= resources['water']:
#         if recipe['coffee'] <= resources['coffee']:
#             if coffee_name != 'espresso':
#                 if recipe['milk'] <= resources['milk']:
#                     resources['milk'] -= recipe['milk']
#                 else:
#                     print(f"Sorry there is not enough milk.")
#                     return False
#             resources['water'] -= recipe['water']
#             resources['coffee'] -= recipe['coffee']
#             return True
#         else:
#             print(f"Sorry there is not enough coffee.")
#             return False
#     else:
#         print(f"Sorry there is not enough water.")
#         return False
#
#
# def process_coins(coffee):
#     print("Please insert coins.")
#     quarters = int(input("how many quarters?: "))
#     dimes = int(input("how many dimes?: "))
#     nickles = int(input("how many nickles?: "))
#     pennies = int(input("how many pennies?: "))
#     total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
#
#     cost = MENU[coffee]['cost']
#     if total < cost:
#         return False
#     else:
#         total -= cost
#         print(f"Here is ${total} in change.")
#         return True
#
#
# earned = 0
# is_over = False
#
# while not is_over:
#     choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
#
#     if choice == 'off':
#         print("Goodbye")
#         exit()
#     elif choice == 'report':
#         print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\n"
#               f"Money: ${earned}")
#     else:
#         if is_resources(choice):
#             is_sufficient_coin = process_coins(choice)
#             if is_sufficient_coin:
#                 earned += MENU[choice]['cost']
#                 print(f"Here is your {choice} ☕. Enjoy!")
#             else:
#                 print("Sorry that's not enough money. Money refunded.")

# ----------------------------------------Angela Yu-------------------
from machine_data import resources, MENU

profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
