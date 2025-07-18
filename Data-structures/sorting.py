temp = [5,6,12,1,62,0,91]
temp_list = []
def sort(direction:bool):
    while len(temp) != 0:
        temp_var = temp[0]
        for i,value in enumerate(temp):
            if direction ==  False and value < temp_var:
                temp_var = value
            elif direction == True and value > temp_var:
                temp_var = value
        temp_list.append(temp_var)
        temp.remove(temp_var)

sort(False)
print(temp_list)