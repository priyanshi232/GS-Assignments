class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    def display_attributes(self):
        attributes = vars(self)
        for attr, value in attributes.items():
            print(f"{attr}: {value}")
# Create an instance of the Student class
student1 = Student(1, "Ram Seeta")
# Display attributes and values
print("Attributes and values before removal:")
student1.display_attributes()
# Remove the student_name attribute
del student1.student_name
# Display attributes and values after removal
print("\nAttributes and values after removal:")
student1.display_attributes()
