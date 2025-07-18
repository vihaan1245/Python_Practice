list = [1,2,7,6,100,1913,141,4,515,63,242]

def linear_search(n):
    for i,value in enumerate(list):
        if value == n:
            print(f"Value found {n}")
            return
    print("Value not found")

linear_search(100)

