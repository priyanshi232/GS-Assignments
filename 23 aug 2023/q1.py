class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary
        return total_salary
    def emp_assign_department(self, new_department):
        self.emp_department = new_department
    def print_employee_details(self):
        print("Employee Details:")
        print(f"Name: {self.emp_name}")
        print(f"ID: {self.emp_id}")
        print(f"Salary: {self.emp_salary}")
        print(f"Department: {self.emp_department}")
# Sample Employee Data
employees = [
    Employee("ADAMS", "E7876", 50000, "ACCOUNTING"),
    Employee("JONES", "E7499", 45000, "RESEARCH"),
    Employee("MARTIN", "E7900", 50000, "SALES"),
    Employee("SMITH", "E7698", 55000, "OPERATIONS")
]
# Using methods to demonstrate functionality
for emp in employees:
    emp.print_employee_details()
    new_department = input(f"Enter new department for {emp.emp_name}: ")
    emp.emp_assign_department(new_department)
    hours_worked = float(input(f"Enter hours worked by {emp.emp_name}: "))
    total_salary = emp.calculate_emp_salary(hours_worked)
    print(f"Total Salary for {emp.emp_name}: {total_salary}\n")





