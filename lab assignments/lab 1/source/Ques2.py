list1 = [("John", ("Physics", 80)), ("Daniel", ("Science", 90)), ("John", ("Science", 95)), ("Mark",("Maths", 100)), ("Daniel", ("History", 75)), ("Mark", ("Social", 95))]
"""print(list1)"""
i = 0
dict1 = {}   # Initializing the variables
val = 0
list2 = []
"""print(list1[1][1])"""
for i in range(len(list1)):
    for j in range(len(list1)):
        if list1[i][0] == list1[j][0]:  # Searching for same student in the lis
            """if i != j:"""
            """print(list1[j][1])"""
            list2.append(list1[j][1])  # Appending all the tuples to a list based on name of a student
    if list1[j][0] not in dict1:
            val = list1[i][0]
            dict1[val] = list2
    list2 = []   # emptying the list for next iteration
    """del list2"""

print(dict1)  # Printing the keys and values present in the dictionary