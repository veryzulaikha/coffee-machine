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


water_quantity = resources["water"]
milk_quantity = resources["milk"]
coffee_quantity = resources["coffee"]
money = 0
sufficient = ""


def money_conversion(penn, nick, dim, quart):
    new_penny = penn * 1
    new_nickel = nick * 5
    new_dime = dim * 10
    new_quarter = quart * 25
    total = new_penny + new_nickel + new_dime + new_quarter
    dollar = float(total / 100)
    return dollar


def income():
    print("Please insert coins.")
    quarter = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nickel = int(input("How many nickels? "))
    penny = int(input("How many pennies? "))
    user_money = money_conversion(penny, nickel, dime, quarter)
    return user_money


def transaction(payment, drink_bill, drink, water_needed, milk_needed, coffee_needed):
    global water_quantity
    global milk_quantity
    global coffee_quantity
    global money
    if payment == drink_bill:
        water_quantity -= water_needed
        milk_quantity -= milk_needed
        coffee_quantity -= coffee_needed
        money += drink_bill
        print(f"Here is your {drink} ☕. Enjoy!")
    elif payment > drink_bill:
        change = round((payment - drink_bill), 2)
        water_quantity -= water_needed
        milk_quantity -= milk_needed
        coffee_quantity -= coffee_needed
        money += drink_bill
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink} ☕. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def shortage(water_needed, milk_needed, coffee_needed):
    global sufficient
    global water_quantity
    global milk_quantity
    global coffee_quantity
    if water_quantity < water_needed:
        sufficient = "no"
        print("Sorry there is not enough water.")
    elif milk_quantity < milk_needed:
        sufficient = "no"
        print("Sorry there is not enough milk.")
    elif coffee_quantity < coffee_needed:
        sufficient = "no"
        print("Sorry there is not enough coffee.")
    else:
        sufficient = "yes"


end = False
while not end:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_order == "espresso":
        bill = MENU["espresso"]["cost"]
        water = MENU["espresso"]["ingredients"]["water"]
        milk = 0
        coffee = MENU["espresso"]["ingredients"]["coffee"]
        shortage(water, milk, coffee)
        if sufficient == "yes":
            user_payment = income()
            transaction(user_payment, bill, user_order, water, milk, coffee)

    elif user_order == "latte":
        bill = MENU["latte"]["cost"]
        water = MENU["latte"]["ingredients"]["water"]
        milk = MENU["latte"]["ingredients"]["milk"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        shortage(water, milk, coffee)
        if sufficient == "yes":
            user_payment = income()
            transaction(user_payment, bill, user_order, water, milk, coffee)

    elif user_order == "cappuccino":
        bill = MENU["cappuccino"]["cost"]
        water = MENU["cappuccino"]["ingredients"]["water"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        shortage(water, milk, coffee)
        if sufficient == "yes":
            user_payment = income()
            transaction(user_payment, bill, user_order, water, milk, coffee)

    elif user_order == "report":
        print(f"water: {water_quantity}ml\nmilk: {milk_quantity}ml\ncoffee: {coffee_quantity}g\nmoney: ${money}")

    elif user_order == "off":
        end = True

    else:
        end = True
