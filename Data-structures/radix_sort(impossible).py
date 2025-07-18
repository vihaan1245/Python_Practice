#74,127,89,73,57,139,80,14,9,3
def radix_sort(arr:list):
    if len(arr) == 1:
        return arr
    max_element = max(arr)
    max_digit = len(str(max_element))
    place = 1
    for i in range(max_digit):
        count_sort(arr,place)
        place *= 10
        print(f"Iteration count : {i+1},  arr:{arr}")
    return arr

def count_sort(arr,place):
    length = len(arr)
    output = [0]*length
    count = [0]*10
    for i in range(length):
        index = (arr[i]//place) % 10
        count[index] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    print(count)
    i = length - 1
    while i >= 0:
        index = (arr[i]//place)%10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(length):
        arr[i] = output[i]

temp = [74,127,89,73,57,139,80,14,9,3]
print(radix_sort(temp))
