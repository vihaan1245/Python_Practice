def shell_sort(arr:list):
    n = len(arr)
    gap = n//2
    while gap > 0:
        print(f"Gap : {gap}")
        for i in range(gap, n):
            selected_number = arr[i]
            j = i
            while j >= gap and arr[j-gap] > selected_number:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = selected_number
        gap //= 2
        print(F"Array : {arr}")

temp = [19,22,15,1,8,2,7,4,11]
shell_sort(temp)
print(temp)

#Gap size = 2
#i = 2 -> selected number is 2, j=2, At the end : arr[j]=2, NO CHANGE, Updated List : []
#i = 1 -> selected number is 5, j=0, At the end : arr[j] = 5, NO CHANGE, Updated List : [2,5,4,3]
#i = 2 -> selected number is 4, j=1, At the end : arr[j] = 4 and after that J value becomes false(Line 9), Updated List : [2,4,5,3]
#i = 3 - > selected number is 3, j = 2, Since 4 > 3, Arr[j] = 3, Updated List : [2,3,4,5]