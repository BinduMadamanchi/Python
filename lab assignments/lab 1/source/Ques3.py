#list of students enrolled in python class
py=input("enter student names in python class")
#list of students enrolled in web class
web=input("enter student names in web class")
a=py.split()
print(a)
b=web.split()
print(b)
#common in both classes
print('Common students in both courses are: ', set(a).intersection(set(b)))
#difference between union and intersection.
print('Not common students are: ', (set(a).union(set(b))).difference(set(a).intersection(set(b))))
