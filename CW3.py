class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.advisor = ""

    def create_new_student(self):
        self.id = int(input("Enter student ID: "))
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")

    def assign_advisor(self, faculty_object):
        self.advisor = faculty_object
        print("Advisor",faculty_object.name, "assigned to student", self.name)

    def display_student(self):
        print("---Student info---")
        print("ID:", self.id)
        print("name:", self.name)
        print("department:", self.department)
        if self.advisor:
            print("advisor:", self.advisor.name)
        else:
            print("Advisor: None")

class Faculty:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.experience = ""
        self.department = ""
        self.course = ""
        self.students_list = []

    def create_new_faculty(self):
        self.id = int(input("Enter faculty ID: "))
        self.name = input("Enter faculty name: ")
        self.experience = int(input("Enter years of experience: "))
        self.department = input("Enter department: ")
        self.course = input("Enter course taught: ")

    def enroll_students(self, student_obj):
        self.students_list.append(student_obj)
        print(f"Student {student_obj.name} enrolled under faculty {self.name}")

    def display_faculty(self):
        print("---Faculty info---")
        print("ID:", self.id)
        print("name:", self.name)
        print("experience:", self.experience, "years.")
        print("department:", self.department)
        print("course:", self.course)
        student_names = [s.name for s in self.students_list]
        print("Assigned Students:", student_names if student_names else "None")

class Course:
    def __init__(self):
        self.department = ""
        self.name = ""
        self.credits = ""
        self.faculty = ""
        self.registered_students = []

    def create_new_course(self):
        self.department = input("Enter department: ")
        self.name = input("Enter name: ")
        self.credits = int(input("Enter credits: "))

    def assign_faculty(self, faculty_object):
        self.faculty = faculty_object
        print("Faculty",faculty_object.name, "assigned to teach", self.name)

    def register_students(self, student_obj):
        self.registered_students.append(student_obj)
        print(f"Student {student_obj.name} registered in course {self.name}")

    def display_course(self):
        print("---Course info---")
        print("department:", self.department)
        print("name:", self.name)
        print("credits:", self.credits)
        print("assigned faculty:", self.faculty.name if self.faculty else "None")
        student_names = [s.name for s in self.registered_students]
        print("Registered Students:", student_names if student_names else "None")



myStudentsList = []
myFacultyList = []
myCoursesList = []

print("1.Create student")
stu = Student()
stu.create_new_student()
myStudentsList.append(stu)

print("2.Create faculty")
fac = Faculty()
fac.create_new_faculty()
myFacultyList.append(fac)

print("3.Create course")
crs = Course()
crs.create_new_course()
myCoursesList.append(crs)

print("4.Relate Objects")
stu.assign_advisor(fac)
fac.enroll_students(stu)
crs.assign_faculty(fac)
crs.register_students(stu)

print("5.Display info")
stu.display_student()
fac.display_faculty()
crs.display_course()
