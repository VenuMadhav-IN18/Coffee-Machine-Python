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
profit=0
def sufficient_resources(ingredients):
    for items in ingredients:
        if ingredients[items]> resources[items]:
            print(f"insuffient items{items}")
            return False
    return True
def process_coins():
    print("insert the coin")
    total=int(input("how many quater?"))*0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def money_sufficient(money_received,drink_cost):
    if money_received>drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("insufficent money")
def make_coffee(drink_name,order_ingedients):
    for item in order_ingedients:
        resources[item] -= order_ingedients[item]
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
        if sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            if  money_sufficient(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



