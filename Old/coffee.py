from sys import exit
import time

print("Welcome to the GOAT Cafe")
print("We ONLY accept cash! Please remember this")
print("Type off if you want to turn the machine off and type report if you want to know about the resources in the cafe")
# Defining ingredient and cost variables
resource = {"Water": 400, "Milk":650, "Coffee Powder":200, "Money":0}

menu = {"espresso":{"Ingredient" : {"Water": 40, "Milk" : 100, "Coffee Powder":50}, "Cost":1.50},
        "latte":{"Ingredient":{"Water": 40, "Milk" : 100, "Coffee Powder":35}, "Cost":2.45},
        "cappuccino":{"Ingredient" : {"Water": 60, "Milk" : 110, "Coffee Powder":29}, "Cost": 1.75}}

def coffee_machine():

    def print_report():
        print("Here is the Report!")
        print(f"Amount of Water Currently Available: {resource['Water']}")
        print(f"Amount of Milk Currently Available: {resource['Milk']}")
        print(f"Amount of Coffee Powder Available: {resource['Coffee Powder']}")
        print(f"Amount of Money Made: ${resource['Money']}")

    def check_resource(order):
        if resource["Water"] < menu[order]["Ingredient"]["Water"]:
            print("Sorry there is not enough water")
            return False
        elif resource["Milk"] < menu[order]["Ingredient"]["Milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif resource["Coffee Powder"] < menu[order]["Ingredient"]["Coffee Powder"]:
            print("Sorry there is not enough coffee powder.")
            return False
        else:
            return True

    def process_coins(order):
        total = 0
        required = menu[order]["Cost"]

        quarters = int(input("Enter the amount of quarters: ")) * 0.25
        total += quarters
        if total >= required:
            return total

        dimes = int(input("Enter the amount of dimes: ")) * 0.10
        total += dimes
        if total >= required:
            return total

        nickels = int(input("Enter the amount of nickels: ")) * 0.05
        total += nickels
        if total >= required:
            return total

        cents = int(input("Enter the amount of cents: ")) * 0.01
        total += cents

        return total

    def check_transaction(order,total):
        cost = menu[order]["Cost"]
        if total >= cost:
            change = round(total-cost,3)
            resource["Money"] += cost
            if change > 0:
                print(f"Here is your {change} change.")
            return True
        else:
            print("Sorry not enough money. The money has been refunded")
            return False

    def make_coffee(order):
        resource["Water"] -= menu[order]["Ingredient"]["Water"]
        resource["Milk"] -= menu[order]["Ingredient"]["Milk"]
        resource["Coffee Powder"] -= menu[order]["Ingredient"]["Coffee Powder"]
        print(f"Here is your {order}. Enjoy!")

    while True:
        order = input("What would you like to order? (espresso, 1.5$ /latte, 2.45$/cappuccino, 1.75$)?: ").lower()

        if order == "off":
            print("Turning the coffee machine off...")
            exit(0)

        elif order == "report":
            print_report()

        elif order in menu:
            if check_resource(order):
                total = process_coins(order)
                if check_transaction(order,total):
                    make_coffee(order)

        else:
            print("Invalid Option. Please choose again")

coffee_machine()
print("Thank you")