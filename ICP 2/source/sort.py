list1 = ["1", "4", "0", "6", "9"]
list2 = []
i = 0
for i in range(len(list1)):
    list2.append(int(list1[i]))
list2.sort()
print(list2[:])