class human:
    def __init__(self, name, emailid):
        self.name = name
        self.email = emailid
    def display(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
class student(human):
    count = 0
    def __init__(self, name, emailid, stud_id):
        human.__init__(self, name, emailid)
        self.stud_id = stud_id
        student.count +=1
    def displayCount(self):
        print("Total no of Students:", student.count)
    def display(self):
        print("Student Details are :")
        human.display(self)
        print("Student Id: ",self.stud_id)
class Librarian1(human):
    StudentCount = 0
    def __init__(self, name, emailid, empl_id):
        super().__init__(name, emailid)
        self.employee_id = empl_id
    def display(self):
        print("Employee Details are:")
        human.display(self)
        print("Employee Id is: ",self.employee_id)
class Book1():
    def __init__(self, Bname, author, bk_id):
        self.book_name = Bname
        self.author = author
        self.book_id = bk_id
    def display(self):
        print("Book Details")
        print("Book_Name: ", self.book_name)
        print("Author: ", self.author)
        print("Book_ID: ", self.book_id)
class Borrow_Buk(student, Book1):
    def __init__(self, name, emailid, stuid, bookname, author, book_id):
        student.__init__(self, name, emailid, stuid)
        Book1.__init__(self, bookname, author, book_id)
    def display(self):
        print("Required Borrowed Book Details:")
        student.display(self)
        Book1.display(self)
store= []
store.append(student('rishu', 'rishu05@gmail.com',2005))
store.append(student('bindu', 'bindum@gmail.com', 1994))
store.append(Librarian1('nitu', 'niteesha97@gmail.com', 909099))
store.append(Librarian1('divya', 'divya9897@yahoo.com', 2008764))
store.append(Book1('web', 'harsha',8635))
store.append(Book1('python', 'sai',9654))
store.append(Borrow_Buk('rishu', 'rishu05@gmail.com', 2005, 'python', 'sai', 9654))
for obj, item in enumerate(store):
    item.display()
    print("\n")
    if obj == len(store)-1:
        item.displayCount()