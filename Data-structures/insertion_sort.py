def insertion_sort(arr:list):
    n = len(arr)
    for i in range(1,n):
        selected_number = arr[i]
        print(f"Selected Number : {selected_number}")
        j = i-1
        while j >= 0 and arr[j] >= selected_number:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = selected_number
        print(F"Arr:{arr}")

temp = [19,22,15,1,8,2,7,4,11]
insertion_sort(temp)
print(temp)

#i = 0 -> selected number is 2, j=-1, At the end : arr[j]=2, NO CHANGE, Updated List : [2,5,4,3]
#i = 1 -> selected number is 5, j=0, At the end : arr[j] = 5, NO CHANGE, Updated List : [2,5,4,3]
#i = 2 -> selected number is 4, j=1, At the end : arr[j] = 4 and after that J value becomes false(Line 9), Updated List : [2,4,5,3]
#i = 3 - > selected number is 3, j = 2, Since 4 > 3, Arr[j] = 3, Updated List : [2,3,4,5]
