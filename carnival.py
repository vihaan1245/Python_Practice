from sys import exit

print("Welcome to the carnival game!")

height = int(input("Enter your height in cm: "))
age = int(input("Enter your age in years: "))
photos = input("Do you want photos after your done with the ride?(yes/no): ")

total_bill = 0

if height < 120:
    print("You cant ride -_-")
    exit(0)
else:
    print("You can ride!")

if age < 12:
    total_bill = total_bill+5
    print(f"Your current bill is {total_bill}")
elif age <= 18:
    total_bill = total_bill + 7
    print(f"Your current bill is {total_bill}")
elif age == 45 and age <=55:
    print(f"Your current bill is {total_bill}")
else:
    total_bill = total_bill + 12
    print(f"Your current bill is {total_bill}")

match photos:
    case "yes":
        total_bill += 3
    case "no":
        total_bill += 0

print(f"Total bill in the end of the ride {total_bill}!")

def display():




