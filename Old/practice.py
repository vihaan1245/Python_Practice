# #Recursion exercise
# from operator import truediv
#
#
# def print_number(num):
#     if num == 0:
#         return 0
#     print_number(num-1)
#     print(num)
#
# number = print_number(10)
# print(number)
#
# def rev_string(normal):
#      if len(normal) == 0:
#          return 0
#      return normal[::-1]
#
# xy = rev_string("sdasdfghjklfghjk")
# print(xy)
#
#
# # def func_palindrome():
# #      palindrome = input("Enter a word to see whether it is a palindrome or not: ")
# #      if palindrome == palindrome[::-1]:
# #          print("It is a palindrome")
# #      else:
# #          print("It is not a palindrome")
# #
# # func_palindrome()
#
# def palindrome(stri,l,r):
#     if l == r:
#         return True
#
#     if stri[l] != stri[r]:
#         return False
#
#     return palindrome(stri, l+1, r-1)
# x = palindrome("Hello",0,4)
# print(x)



#DECORATER EXERCISES
# def multiply_decorate(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with arguments {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function name {func.__name__} returned {result} value.")
#     return wrapper
#
# @multiply_decorate
# def multiply(*args):
#     result = 1
#     for i in args:
#         result = result * i
#     return result
#
# @multiply_decorate
# def add(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
# multiply(10,10,10)
# add(10,10,10)
#
#
#
# import time
#
# def measure_func(func):
#     def wrapper(n):
#         start_time = time.time()
#         func(n)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"The amount of time {func.__name__} took is {execution_time: .6f} ")
#     return wrapper
#
# @measure_func
# def example_func(n):
#     total = 0
#     for i in range(1,n+1):
#         total += i+n
#     return total
#
# example_func(10000)
#
# def double(x):
#     return 2*x
#
# def triple(x):
#     return 3*x
#
# def apply_function(func,x):
#     return func(x)
#
# print(apply_function(double,5))
# print(apply_function(triple,5))

#Airport
# data = {
#     "US": {
#         "New York": "John F. Kennedy International Airport (JFK)",
#         "Los Angeles": "Los Angeles International Airport (LAX)",
#         "Chicago": "O'Hare International Airport (ORD)"
#     },
#     "Canada": {
#         "Toronto": "Toronto Pearson International Airport (YYZ)",
#         "Vancouver": "Vancouver International Airport (YVR)",
#         "Montreal": "Montreal-Pierre Elliott Trudeau International Airport (YUL)",
#         "Calgary": "Calgary International Airport (YYC)",
#         "Ottawa": "Ottawa Macdonald-Cartier International Airport (YOW)"
#     },
#     "UK": {
#         "London": "Heathrow Airport (LHR)",
#         "Gatwick": "Gatwick Airport (LGW)",
#         "Manchester": "Manchester Airport (MAN)",
#         "Birmingham": "Birmingham Airport (BHX)",
#         "Edinburgh": "Edinburgh Airport (EDI)"
#     },
#     "Australia": {
#         "Sydney": "Sydney Kingsford Smith Airport (SYD)",
#         "Melbourne": "Melbourne Airport (MEL)",
#         "Brisbane": "Brisbane Airport (BNE)",
#         "Perth": "Perth Airport (PER)",
#         "Adelaide": "Adelaide Airport (ADL)"
#     },
#
#     "Germany": {
#         "Berlin": "Berlin Brandenburg Airport (BER)",
#         "Munich": "Munich Airport (MUC)",
#         "Frankfurt": "Frankfurt Airport (FRA)",
#         "Hamburg": "Hamburg Airport (HAM)"
#     },
#     "France": {
#         "Paris": "Charles de Gaulle Airport (CDG)",
#         "Nice": "Nice Côte d'Azur Airport (NCE)",
#         "Lyon": "Lyon-Saint Exupéry Airport (LYS)",
#         "Marseille": "Marseille Provence Airport (MRS)"
#     },
#     "Japan": {
#         "Tokyo": "Narita International Airport (NRT)",
#         "Osaka": "Kansai International Airport (KIX)",
#         "Nagoya": "Chubu Centrair International Airport (NGO)",
#         "Sapporo": "New Chitose Airport (CTS)"
#     },
#     "Brazil": {
#         "São Paulo": "São Paulo/Guarulhos–Governador André Franco Montoro International Airport (GRU)",
#         "Rio de Janeiro": "Rio de Janeiro/Galeão International Airport (GIG)",
#         "Brasília": "Brasília International Airport (BSB)"
#     },
#
# "India": {
#         "Delhi": "Indira Gandhi International Airport (DEL)",
#         "Mumbai": "Chhatrapati Shivaji Maharaj International Airport (BOM)",
#         "Bangalore": "Kempegowda International Airport (BLR)",
#         "Chennai": "Chennai International Airport (MAA)",
#         "Kolkata":"Subhas chandra bose int airport"
#     }
# }
#
#
# def get_airport(location):
#     for countries,cities in data.items():
#         if location in cities:
#             return f"Airport in {location} is {cities[location]}"
#         elif location in countries:
#             return "\n".join([f"{city}: {airport}" for city, airport in cities.items()])
#     return "Location not found"
#
# while True:
#     location = input("Enter a city or country name (or 'exit' to quit): ").strip()
#     if location.lower() == 'exit':
#         break
#     result = get_airport(location)
#     print(result)

#Undo and Redo FUnction
undo_list = []
redo_list = []

def perform(action):
    undo_list.append(action)
    redo_list.clear()
    return f"Performed Action is {action}"

def undo():
    if undo_list:
        action_to_undo = undo_list.pop()
        redo_list.append(action_to_undo)
        return f"Undid the {action_to_undo}"
    else:
        return "No action to undo"

def redo():
    if redo_list:
        last_action = redo_list.pop()
        undo_list.append(last_action)
        return f"Redid the action {last_action}"
    else:
        return "No action to redo"

def display_lists():
    return f"List: {undo_list}"

while True:
    user_input = input("Enter undo,redo and display to display the list and exit to quit the program: ")

    if user_input.lower() == "undo":
        print(undo())
    elif user_input.lower() == "redo":
        print(redo())
    elif user_input.lower() == "exit":
        break
    elif user_input.lower() == "display":
        print(display_lists())
    else:
        print(perform(user_input))
        print(display_lists())


