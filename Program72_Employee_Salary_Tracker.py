# Employee Salary Tracker
#Create a class Employee with name, designation, and monthly salary. Add a method to calculate the annual salary and print the employee details

class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def calc_annual_salary(self):
        annual_salary = self.salary*12
        return annual_salary

    def display(self):
        print(f"Details of {self.name} are as follows: \nName: {self.name}\nDesignation: {self.designation} \nMonthly Salary: {self.salary} \nAnnual Salary: {self.calc_annual_salary()} ")


name = input("Please enter the name: ")
designation = input("Please enter the Designation: ")
m_salary = input("Please enter the Monthly Salary: ")
employee1 = Employee(name, designation, int(m_salary))

employee1.display()