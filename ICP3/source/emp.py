class Employee:  
    empCount = 0
    totsal = 0
    avgsal = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.empCount += 1
        Employee.totsal += int(salary)

    def average_salary(self):
        print("average salary of %d" % (Employee.totsal / Employee.empCount))

    def print_emp(self):
        print("\nName:", self.name, "\nFamily:", self.family, "\nSalary:", self.salary, "\nDepartment:", self.department)

class Fulltime_Employee(Employee):
    def child_method(self):
        print("child class")


emp1 = Employee("Bindu", "family1 ", "100", "Dep1")
emp2 = Employee("Rishitha", "family2", "200", "Dep2")
emp3 = Employee("Divya", "family3", "300", "Dep3")
emp4 = Fulltime_Employee("Bindu", "family4", "400", "Dep4")

print("Total Employee %d" % Employee.empCount)
print("average salary of %d" % (Employee.totsal / Employee.empCount))
# this is by function calling
emp3.average_salary()
emp1.print_emp()
emp4.child_method()