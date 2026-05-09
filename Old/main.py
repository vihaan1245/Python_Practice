import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9','10','0']
special = ["_","(","*","&","^","%","$","#","@","!"]


input1 = int(input("Enter amount of characters you want for your password:"))
input_characters = int(input("Enter how many letters do you want in your password:"))
input_numbers = int(input("Enter how many numbers you want:"))
input_special = int(input("Enter how many special characters:"))

final_password = ""

if input_characters + input_numbers + input_special != input1:
    print("Error: The total number of characters does not match your inputs (Just saying).")

else:
    password = random.choices(letters, k=input_characters)
    password1 = random.choices(numbers, k=input_numbers)
    password2 = random.choices(special, k=input_special)

    final_password = password + password1 + password2

    random.shuffle(final_password)

    final_password = ''.join(final_password)
    print(type(final_password))
    print(f"Your final password is {final_password}")





