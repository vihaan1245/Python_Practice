#Lists
def to_do_list():
    chores = []
    while True:
        chore_input = input("Enter a task for your to do list (stop to stop the program and type see to check the list). Press enter when done: ")
        if chore_input == "stop".lower():
            return False

        elif chore_input == "see":
            print("\nYour To-Do List:")
            for task in chores:
                print(f"{task}")

        else:
            chores.append(chore_input)
            print("Task added")

to_do_list()

#Dictonaries
print("First Execution")
dictionary = {"Vihaan":"Likes to play football and is quite comical", "Suhaan":"Good at football and has aura and my best friend","Rishit":"Quite the weird little person"}
for k,v in dictionary.items():
    print(k, ":", v)

print("")

print("Second Execution")
dictionary.update({"Dhyan":"Quite the sports enthusiast and my best friend"})
dictionary["Rishit"] = "Shifted to South Bombay and my best friend"

for k,v in dictionary.items():
    print(k, ":", v)

#Tuples
tuple = [("The code for O’Hare International Airport is", "ORD."),
         ("The code for Los Angeles International Airport is", "LAX."),
         ("The code for Dallas/Fort Worth International Airport is","DFW."),
         ("The code for Denver International Airport is","DEN.")]
for name,code in tuple:
    print(f"{name} {code}")
