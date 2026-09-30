class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""

    def create_new_student(self):
        self.id = int(input("Enter student ID: "))
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")

    def display_student(self):
        print("ID:", self.id)
        print("name:", self.name)
        print("department:", self.department)

class Faculty:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.experience = ""
        self.department = ""
        self.course = ""


    def create_new_faculty(self):
        self.id = int(input("Enter faculty ID: "))
        self.name = input("Enter name: ")
        self.experience = int(input("Enter years of experience: "))
        self.department = input("Enter department: ")
        self.course = input("Enter course: ")


    def display_faculty(self):
        print("ID:", self.id)
        print("name:", self.name)
        print("experience:", self.experience)
        print("department:", self.department)
        print("course:", self.course)

class Course:
    def __init__(self):
        self.department = ""
        self.name = ""
        self.credits = ""

    def create_new_course(self):
        self.department = input("Enter department: ")
        self.name = input("Enter name: ")
        self.credits = int(input("Enter credits: "))

    def display_course(self):
        print("department:", self.department)
        print("name:", self.name)
        print("credits:", self.credits)



myStudent = []  #store student objects

stu = Student()

stu.create_new_student()
stu.display_student()

myStudent.append(stu) #new
print(myStudent)


