# # def my_decorater(func):
# #     def wrapper():
# #         print("2uPac")
# #         func()
# #         print("asdfghjk")
# #     return wrapper
# #
# # @my_decorater
# # def hello_world():
# #     print("Hello World")
# #
# # hello_world()
# def smart_divide(func):
#     def wrapper(x,y):
#         if func.__name__ == "divide":
#             print("Division: ")
#         elif func.__name__ == "add":
#             print("Addition: ")
#
#         if func.__name__ == "divide" and y == 0:
#             raise ValueError
#         else:
#             return func(x,y)
#     return wrapper
#
# @smart_divide
# def divide(x,y):
#     return x/y
#
# @smart_divide
# def add(x,y):
#     return x+y
#
# print(divide(9,3))
# print(add(9,3))
