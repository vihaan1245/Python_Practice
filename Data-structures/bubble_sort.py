def bubble_sort(arr:list):
    for i in range(len(arr)-1):
        for j in range((len(arr)-1)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
temp = [12,3,24,22,13,9,2,6]
bubble_sort(temp)
print(temp)

#j=0 -> 12,3 is compared, Updated List : 3,12,24,22,13,9,2,6
#j=1 -> 12,24 is compared, Updated List : 3,12,24,22,13,9,2,6
#j=2 -> 24,22 is compared, Updated List : 3,12,22,24,13,9,2,6
#j=3 -> 24,13 is compared, Updated List : 3,12,22,13,24,9,2,6
#j=4 -> 24, 9 is compared, Updated List : 3,12,22,13,9,24,2,6
#j=5 -> 24,2 is compared, Updated List : 3,12,22,13,9,2,24,6
#j=6 -> 24,6 is compared, Updated List : 3,12,22,13,9,2,6,24

#Homework - [1,2,3,4,5,7,6]
def Optimized_bubble_sort(tempo:list):
    for i in range(len(tempo)-1):
        swapped = False
        print(i)
        for j in range((len(tempo)-1)-i):
            if tempo[j] > tempo[j+1]:
                tempo[j],tempo[j+1] = tempo[j+1], tempo[j]
                swapped = True
        print(tempo)
        if not swapped:
            break
        return tempo

hw = [1,2,3,4,5,7,6]
Optimized_bubble_sort(hw)

