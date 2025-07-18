def selection_sort(arr:list):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

temp = [1,5,3,9,6,4,7,2,8]
selection_sort(temp)
print(temp)