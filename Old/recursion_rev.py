def fun(n):
    if n > 0:
        print("Before function call :",n)
        fun(n-1)
        print("After function call:",n)

# fun(4)

def factorial(n):
    print(n)
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

# result = factorial(5)
# print(result)

def factorial_tail(n,accumulator=1):
    print(n)
    print(accumulator)
    if n==1 or n==0:
        return accumulator
    else:
        return factorial_tail(n-1, n*accumulator)

# result = factorial_tail(5)
# print(result)

def factorial_loops(n):
    result=1
    for i in range(1,n+1):
        result *= i
    print(result)
# factorial_loops(5)

# 5%2=1
# 2%2=0
# 1%2=1
#
# 10%2=0
# 5%2=1
# 2%2=0
# 1%2=1
# 1010
#Binary number to real number conversion

def binary_number_converter(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return binary_number_converter(n//2) + str(n%2)

result = binary_number_converter(50)
print(result)