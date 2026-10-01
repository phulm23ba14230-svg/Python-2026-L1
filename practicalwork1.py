class Student:
    def __init__(self, student_id, name, Dob):
        self.student_id = student_id 
        self.name = name
        self.Dob = Dob
class course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
class mark:
    def __init__(self,student_id, course_id,mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark
def input_student():
    student = []
    n = int(input("Enter number of student:"))
    for i in range(n):
        print(f"\nStudent (i+1)")
        student_id = input("Enter student ID:")
        name = input("Enter name:") 
        Dob = input("Enter Dob:")
        student = Student(student_id, name, Dob)
        student.append({"student_id:"})
    return student
def input_course():
    course = []
    n = int(input("\nEnter number of course:"))
    for i in range(n):
        print(f"\nCourse (i= 1)")
        course_id = input("Enter course ID:")
        course_name = input("Enter course name:")
        course = course(course_id, course_name)
        course.append(Student)
    return course
def input_marks(students, courses):
    mark = []
    print("\n==== ENTER MARKS ====")
    for student in students:
        for course in courses:
            print(f"\nStudent: (student.name)")
            print(f"\nCourse: (course.course_name)")
            mark = float (input("Enter mark:"))
            mark.append(
                mark(
                    student.student_id,
                    course.course_id,
                    mark
                )
            )
    return mark
def list_students(students):
    print("\n==== STUDENT LIST ====")
    print(f"{'ID':<15}{'Name':<25}{'Date of birth':<15}")
    for student in students:
        print(
            f"{student.student_id:<15}"
            f"{student.name:<25}"
            f"{student.dob:<15}"
        )    
def list_course(courses):
    print("\n==== COURSE LIST====")
    print(f"{'ID':<15}{'Course Name':<25}")
    for course in courses:
        print(
            f"{course.course_id:<15}"
            f"{course.course_name:<25}"
        )
def list_marks(marks, students, courses):
    print("\n==== MARK LIST ====")
    print(
        f"{'Student ID':<15}"
        f"{'Student Name':<25}"
        f"{'Mark':<15}"
    )
    for mark in marks:
        if mark.course_id == course.course_id:
            student_name = ""
            for student in students:
                if student.student_id == mark.student_id:
                    student_name = student.name
            print(
                f"{mark.student_id:<15}"
                f"{student_name:<25}"
                f"{mark.mark:<10.2f}"
            )

students = input_student()
courses = input_course ()
marks = input_marks(students, courses)
while True:
    print("\n=====================")
    print(" STUDENT MARK MANAGEMENT")
    print("=====================")
    print("1. List students")
    print("2. List courses")
    print("3. List marks")
    print("4. Show mark of a course")
    print("5. EXIT")
    choice = input("Enter your choice:")
    if choice == "1":
        list_students(students)
    elif choice == "2":
        list_course(courses)
    elif choice == "3":
        list_marks(marks, students, courses)

    elif choice == "4":
        show_courses_marks(marks, students, courses)
    elif choice == "5":
        print("Program terminated.")
        break
    else:
        print("Invalid choice!")



