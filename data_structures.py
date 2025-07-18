def number(n):
    total = 0
    for num in n:
        total += num
    return total

n = [1,2,3,4,5,6,7]
result = number(n)
print(result)

def print_pairs(n):
    total = 0
    for num in n:
        total += num
    print(total)
    for i in range(len(n)):
        for x in range(len(n)):
            print(f"Pair : ({n[i]}, ({n[x]})")

n = [1,2,3]
print_pairs(n)


