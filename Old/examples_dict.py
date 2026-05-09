# # dict = {"Name":"Vihaan", "Age":14, "State":"Mumbai"}
# # print(dict)
# # dict.update({"Age":16})
# # print(dict)
# # dict.update({"Country":"India"})
# # print(dict)
# #
# # dict.pop("Country")
# # print(dict.keys())
# # print(dict)
# #
# # dict.popitem()
# # print(dict)
# list = ["skibidi","country","nation"]
# list1 = ["A","b","c","d",1,5,7,"A"]
#
# # list1.reverse()
# # print(list1)
#
# list1.remove("A")
# print(list1)
#
# list1.pop(3)
# print(list1)
#
# list1.extend(list)
# print(list1)
#
# list.append("A")
# print(list)
#
# list.insert(2,"A")
# print(list)
#
# #0,1,4,9,16,25,36,49,64
#
# square = []
#
# for i in range(0,11):
#     square.append(i*i)
#     i += 1
#
# print(square)

square2 = [i**2 for i in range(11)]
print(square2)

#(n+1) + (n-2)
fib_list = [1,1]
[fib_list.append(fib_list[i-2]+fib_list[i-1])for i in range(2,11)]
print(fib_list)

list5 = [5,-1,9,-10,5,8,3,-10,-6,-7]
# list_num = []
# new_l = []

new_list = ["positive" if x > 0 else "negative" for x in list5]
print(new_list)

# for i in list5:
#     if i >= 0:
#         list_num.append("p")
#     else:
#         list_num.append("n")
# print(list5)
# print(list_num)

# for i in range(1,11):
#     if i % 2 == 0:
#         new_l.append("p")
#     else:
#         new_l.append("n")
#
# print(new_l)
