# def add_function(*args):
#     sum = 0
#     for arg in args:
#         sum = sum + arg
#     return sum
#
# a = add_function(1,2,3,4,5,6,7,8)
# print(a)
#
# def add(**kwargs):
#     sum = 0
#     for key,value in kwargs.items():
#         sum = sum+value
#     return sum
#
# b = add(a=1,b=2,c=3,f=4,e=1353)
# print(b)
#
# menu = {"Espresso":{"Ingredient" : {"Water": 40, "Milk" : 100, "Coffee Powder":50}, "Cost":1.50},
#         "Latte":{"Ingredient":{"Water": 40, "Milk" : 100, "Coffee Powder":35}, "Cost":2.45},
#         "Cappuccino:":{"Ingredient" : {"Water": 60, "Milk" : 110, "Coffee Powder":29}, "Cost": 1.75}}
#
# print(menu["Espresso"]["Ingredient"]["Water"])
#
# add = lambda x,y : x+y
# ty=add(1,2)
# print(ty)
# print(type(add))

# def gen_func(num):
#     for i in range(1,num+1):
#         yield i
#
# x = gen_func(1000)
# for i in x:
#     print(i)


# def add1(num):
#     sum=0
#     for i in range(1,num+1):
#         sum = sum + i
#     return sum
#
# yz = add1(5)
# print(yz)
#
# def add2(num):
#     if num == 0:
#         return 0
#     return num + add2(num-1)
#
# xyz = add2(6)
# print(xyz)

# def factorial(num):
#     factorial1 = 1
#     for i in range(1,num+1):
#         factorial1 = factorial1 * i
#     return factorial1
#
# fact = factorial(5)
# print(fact)

# def factorial_recur(num):
#     if num <= 1:
#         return 1
#     return num * factorial_recur(num-1)
#
# number = factorial_recur(5)
# print(number)

#0,1,1,2,3,5,8,13,21,34
# def fib_func(num):
#     list = [0,1]
#     for i in range(2,num+1):
#         list.append(list[-1] + list[-2])
#     return list
#
# number = fib_func(10)
# print(number)

# def fib_gen(num):
#     a=0
#     b=1
#     for i in range(num):
#         yield a
#         #a,b = b, a+b
#         temp = a
#         a = b
#         b = temp + b
#
# asd = fib_gen(10)
#
# # for i in asd:
# #     print(i)

def fib_rec(num):
    if num <= 1:
        return 1
    return fib_rec(num-1) + fib_rec(num-2)

for i in range(10):
    print(fib_rec(i))
