def pivot(arr:list,left,right):
    pivot_value = arr[right]
    print(f"Pivot value : {pivot_value}")
    temp_index = left-1
    for i in range(left,right):
        print(f"Arr[i] : {arr[i]}")
        if arr[i] < pivot_value:
            temp_index += 1
            arr[temp_index], arr[i] = arr[i], arr[temp_index]
            print(f"Printing Array : {arr}")
    arr[temp_index+1], arr[right] = arr[right],arr[temp_index+1]
    return temp_index + 1

def quick_sort(arr:list, left, right):
    print(f"Left : {left}, Right : {right}, Array :{arr}")
    if left < right:
        pivot_index = pivot(arr,left,right)
        print(f"Pivot Index : {pivot_index}")
        quick_sort(arr,left,pivot_index-1)
        quick_sort(arr,pivot_index+1,right)

temp = [8,6,5,7,4,1]
quick_sort(temp,0,len(temp)-1)
print(temp)
