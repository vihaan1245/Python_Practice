import math

def binary_search(data:list, n):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = math.floor((low + high) / 2)
        if n == data[mid]:
            print("Value found")
            return
        elif n < data[mid]:
            high = mid-1
        elif n > data[mid]:
            low = mid+1
    print("Value not found")
binary_search([11,22,33,44,55,76,87,98],11)

# low = 0
# high = 7
# mid = 3 -> 44
# mid != 55
# low = 4 -> 55
# mid=5 -> 76
# low = mid+1 - > 6 - > 87
# mid=6 - > 87
# low = mid+1 -> 7 -> 98

#low=0
#high = 7
# mid = 3 -> 44
# high = 2 -> 33
# mid = 1 -> 22
# high = 0 -> 11
# mid = 0 -> 11
# 11 = 11

def binary_recursive(data:list[int], target,low,high):
    if low > high:
        print("Value not found")
    else:
        mid = math.floor((low+high)/2)
        if data[mid] == target:
            print(f"Value found : {target}")
            return mid
        elif target < data[mid]:
            return binary_recursive(data,target,low,mid-1)
        elif target > data[mid]:
            return binary_recursive(data,target,mid+1,high)


array = [11,12,13,15,21.45,49,80]
result = binary_recursive(array,35,0,high=len(array)-1)

