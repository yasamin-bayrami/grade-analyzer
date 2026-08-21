import json
class Student:
    def __init__(self, name,grade):
        self.name = name
        self.grade = grade 
    def passed(self):
            if self.grade>= 50:
                return True
            else:
                return False
    def to_dict(self):
        return {
            "name": self.name,
            "grade": self.grade
    }
            


def add_student(students):
    name = input("What is the student's name: ")

    try:
        grade = int(input("What is the student's grade: "))
    except ValueError:
        print("Please enter a number for the grade.")
        return

    new_student = Student(name, grade)
    students.append(new_student)
    save_students(students)

def save_students(students):
    student_data = []

    for student in students:
        student_data.append(student.to_dict())

    with open("students.json", "w") as file:
        json.dump(student_data, file)

def load_students():
    try:
        with open("students.json", "r") as file:
            student_data = json.load(file)

        students = []

        for item in student_data:
            new_student = Student(item["name"], item["grade"])
            students.append(new_student)

        return students

    except FileNotFoundError:
        return []
students = load_students()

def find_student(students):
    search_name = input("Enter the student's name: ")

    for student in students:
        if student.name.lower() == search_name.lower():
            print(f"{student.name}: {student.grade}")
            return

    print("Student not found.")

def show_students (students):
     if len(students) == 0:
        print("No students added yet.")
        return

     for student in students:
        print(f"{student.name}: {student.grade}, Passed: {student.passed()}")


def average_grade(students):
     if len(students) == 0:
        print("No students added yet.")
        return

     total = 0

     for student in students:
        total += student.grade

     average = total / len(students)
     return average

def best_grade(students):
     if len(students) == 0:
        print("No students added yet.")
        return

     return max(student.grade for student in students)

 
def best_student (students):
     if len(students) == 0:
        print("No students added yet.")
        return

     return max(students, key=lambda student: student.grade)


def show_passing_students(students):
     if len(students) == 0:
        print("No students added yet.")
        return

     for student in students:
        if student.passed():
            print(student.name)



while (True):
    user= input("what would you like to do?\n 1-get the students names,grades and if they have passed \n 2-get the average of the grades\n 3-get the best grade\n 4-see who got the best grade\n 5-see who passed\n 6-add a student\n 7-find a student\n 8-exit\n")
    
    if user=="1" :
        show_students(students)
    elif user=="2":
        print(f"Average grade: {average_grade(students)}")
    elif user=="3":
        print (best_grade(students))
    elif user=="4":
        top_student = best_student(students)

        if top_student is not None:
          print(top_student.name)
    elif user=="5":
        show_passing_students(students)
    elif user=="6":
        add_student(students)
    elif user=="7":
        find_student(students)
    elif user=="8":
        break
