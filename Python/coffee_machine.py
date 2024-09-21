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

money = {
    "value": 0,
}
profit = 0
is_on = True



def is_resource_sufficient(order_ingredients):
    """ Returns the total calculated from coins inserted."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
          print(f"Sorry, there's not enough {item}")
          is_enough = False
    return is_enough

def process_coins():
    print("Please inset coins.")
    """Returns the total calculated from coins inserted."""
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many quarters?")) * 0.05
    total += int(input("How many quarters?")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or false money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change,")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough money, please accept the refund")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice} ☕")

while is_on:
    choice = input("What would you like? Type 'espresso', 'latte', 'cappuccino': ").lower()
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

