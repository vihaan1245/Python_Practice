#Exercise 1
expenses = [2200,2350,2600,2130,2190]

feb_spent = expenses[1] - expenses[0]
print(f"Amount spent in february compared to January is {feb_spent}")

quarterly_expense = expenses[0] + expenses[1] + expenses[2]
print(f"Quarterly expenses : {quarterly_expense}")

spent_2000 = 2000 in expenses
print(f"Did you spend exactly 2000 dollars in any month? {spent_2000}")

expenses.append(1980)
print(f"Amount spent is June is {expenses[5]}")

expenses[3] += 300
for i,expense in enumerate(expenses):
    print(f"Index {i}: ${expense},", end=" ")

#Exercise 2
heroes=['spider man','thor','hulk','iron man','captain america']
print(f"Length of the list : {len(heroes)}")

heroes.append('black panther')
print("List after appending 'black panther':", heroes)

heroes.remove('black panther')
heroes.insert(3, 'black panther')
print("List after placing 'black panther' after 'hulk':", heroes)

heroes = ['doctor strange' if hero in ['thor', 'hulk'] else hero for hero in heroes]
heroes.remove('doctor strange')
print("List after replacing 'thor' and 'hulk' with 'doctor strange':", heroes)

heroes.sort()
print("Sorted List : ", heroes)