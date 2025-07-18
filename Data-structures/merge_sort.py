def merge_sort(arr:list):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    print("Left",left_arr)
    print("Right",right_arr)
    return merge(merge_sort(left_arr), merge_sort(right_arr))

def merge(left,right):
    print("LEFT",left)
    print("RiGTH", right)
    l = len(left)
    r = len(right)
    left_index = 0
    right_index = 0

    final = []
    while left_index < l and right_index < r:
        if left[left_index] < right[right_index]:
            final.append(left[left_index])
            print(final)
            left_index += 1
        else:
            final.append(right[right_index])
            print(final)
            right_index += 1

    return final+left[left_index:]+right[right_index:]

temp = [6,1,5,3]
print(merge_sort(temp))

# Explanation:
# The array is split into two halves again and again until each part has only one element.
# For example, [6, 1, 5, 3] is split into [6, 1] and [5, 3], then into [6], [1], [5], and [3].
# The `merge` function puts these smaller arrays back together in the correct order.
# `left_index` and `right_index` are used to keep track of where we are in the left and right arrays.
# The while loop compares the first number from the left array with the first number from the right array.
# If the left number is smaller, it’s added to the result, and we move to the next number in the left array.
# If the right number is smaller, it’s added instead, and we move to the next number in the right array.
# After the loop, any leftover numbers in the left or right array are added to the result.
# This is done with `final + left[left_index:] + right[right_index:]`.


