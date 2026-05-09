#1. You are given an integer N. Print numbers from 1 to N without the help of loops.
# Python3 program to Print
# numbers from 1 to n`
# def print_numbers(n):
#     if n <= 0:
#         return
#     print_numbers(n-1)
#     print(n)
#
# print_numbers(5)


# #2. Write a recursive function to print the reverse of a given string.
# # Python program to reverse a string using recursion
# def string_reverse(text):
#     if len(text) <= 0:
#         return
#     temp = text[0]
#     string_reverse(text[1:])
#     print(temp, end="")
#
# string_reverse("human")
# print()


#3. Coin Change – Count Ways to Make Sum  - Complex
# Recursive Python3 program for
# coin change problem.
# Returns the count of ways we can sum
# coins[0...n-1] coins to get sum "sum"
def count(coins,n,target_sum):
    if target_sum == 0:
        return 1
    if target_sum < 0:
        return 0
    if n <=0:
        return 0

    temp_1 =count(coins,n-1,target_sum)
    temp_2 = count(coins,n,target_sum - coins[n-1])
    return  temp_1 + temp_2

coins = [1,2,3,4,5]
sum=4
result = count(coins,len(coins),sum)
print(result)


#4. Recursive function to check if a string is palindrome
# A recursive Python program
# to check whether a given
# number is palindrome or not
# def number_palindrome(number,reverse=0):
#     if number == 0:
#         return reverse
#
#     reverse = reverse * 10 + number % 10
#     return number_palindrome(number//10,reverse)
#
# original_number = 121
# if number_palindrome(original_number):
#     print("Palindrome")
# else:
#     print("No palindrome")
#
#
# # A recursive function that
# # check a str[s..e] is
# # palindrome or not.
# def palindrome(s):
#     if len(s) <= 1:
#         return True
#
#     if s[0].lower() != s[-1].lower():
#         return False
#     else:
#         return palindrome(s[1:-1])
#
# string = "Madam"
# if palindrome(string):
#     print("It is a palindrome")
# else:
#     print("Not a palindrome")
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome(head: Optional[ListNode]) -> bool:
    if len(head) <= 1:
        return True
    if head[0] != head[-1]:
        return False
    return isPalindrome(head[1:-1])
p = [1,2,2,1]
if isPalindrome(p):
    print("palindrome")
else:
    print("not an palindrome")