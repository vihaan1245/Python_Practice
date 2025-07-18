import math
from math import factorial

# #square numbers
# square = [i**2 for i in range(11)]
# print(square)
#
# #convert temperatures
# temp = [0,10,20,30,40]
# temp_fahrenheit = [(9/5)*i + 32 for i in temp]
# print(temp_fahrenheit)
#
# #Even numbers
# even_num = [f"{i}" if i % 2 ==0 else None for i in range(1,22)]
# even_num = [x for x in even_num if x is not None]
# print(even_num)
#
# #Uppercase letters
# letters = ["a","b","A","F","N","q","p","s","i","J","R","K"]
# upper_letters = [i for i in letters if i.isupper()]
# print(upper_letters)
#
# #double numbers
# numbers = [i*2 for i in range(1,11)]
# print(numbers)
#
# #List of lengths
# sentence = input("Enter a normal sentence: ")
# list_sentence = [len(sentence)]
# print(f"Number of characters in the sentence are : {list_sentence}")

#Words with starting with "A" Letter
# word = input("Enter any word: ")
# list_A = [f"The word {word} starts with letter A" if word[0].lower() == "a" else f"The {word} does not start with the letter A"]
# print(list_A)

#Square root of numbers
# root = [math.sqrt(i) for i in range(1,11)]
# print(root)
#
#Add 5 to each number
# add_five = [i+5 for i in range(0,21)]
# print(f"Each number has been added by 5 from 0-20 and the result is {add_five}")

#Get odd length words
# sentence = input("Enter a normal sentence: ")
# odd_length = [i for i in sentence.split() if len(i) % 2 != 0]
# print(odd_length)

#Flatten a list of lists
# list1 = [1,2,3]
# list2 = [1,2,3,4,5,6,7]
# flatten_list = [item for list6 in (list1,list2) for item in list6]
# print(flatten_list)

#Filter negative numbers
# odd_num = [f"{i}" if i % 2 != 0 else None for i in range(1,11)]
# odd_num = [i for i in odd_num if i is not None]
# print(odd_num)

#Get initials
# ini = ["Alice","Landon","Norris","Ray","Sydney","Ken","Carson"]
# first_letter = [f"Initial of {i} is {i[0]}" for i in ini if i[0].isupper()]
# print(first_letter)

#Numbers
# numbros = [12,34,56]
# sum_numbers = [sum(int(digit) for digit in str(num)) for num in numbros]
# print(sum_numbers)

#Filter palindromic words
# palin = input("Enter a word: ")
# palindrome = [f"{palin} is a palindrome" if palin==palin[::-1] else f"{palin} is not a palindrome" ]
# print(palindrome)
#
# #Square of even numbers
# square_even = [f"{i**2}" if i % 2 == 0 else None for i in range(1,11)]
# square_even = [x for x in square_even if x is not None]
# print(square_even)
#
# # Prime Numbers Under 20
# prime_numbers = [num for num in range(2, 20) if all(num % i != 0 for i in range(2, num))]
# print(prime_numbers)
#
# #Multiplication table
# nums = [1,2,3]
# table = [[f"{num} * {i} = {num * i}" for i in range(1,11)] for num in nums]
# print(table)
#
# #Fibonnaci list
# fib_list = [1,1]
# [fib_list.append(fib_list[i-2]+fib_list[i-1])for i in range(2,11)]
# print(fib_list)
#
# #Filter non-alphabetic characters
# sentence = "ABC1234!@"
# filter_sentence = [char for char in sentence if char.isalpha()]
# print(filter_sentence)

# #cartesian product
# integer_list = [1,2,3]
# alphabet_list = ["A","B","C"]
# cartesian_product = [(x,y) for x in integer_list for y in alphabet_list]
# print(cartesian_product)
#
# #zip two lists
# zipped = [(x,y) for x,y in zip(integer_list, alphabet_list)]
# print(zipped)



#custom zip with alternation
# int_list = [10,11,12,13]
# secondint_list = [1,2,3,4]
# for i,(x, y) in enumerate(zip(int_list, secondint_list)):
#     print(i,x,y)
# alternation_zipped = [x if i%2 == 0 else y for i,(x,y) in enumerate(zip(int_list,secondint_list))]
# print(alternation_zipped)

#factorial
factorial = {0:1}
[factorial.update({x:x*factorial[x-1]}) for x in range(1,6)]
print(factorial)
