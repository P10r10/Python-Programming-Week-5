# First write a function named add_student, which adds a new student to the
# database. Also write a preliminary version of the function print_student,
# which prints out the information of a single student.
# After that write a function named add_course, which adds a completed
# course to the information of a specific student in the database. The course
# data is a tuple consisting of the name of the course and the grade
# Courses with grade 0 should be ignored when adding course information.
# Additionally, if the course is already in the database in that specific
# student's information, the grade recorded in the database should never be
# lowered if the course is repeated.
# Please write a function named summary, which prints out a summary based on
# all the information stored in the database.

def add_student(students: dict, name: str):
    students[name] = []


def print_student(students: dict, name: str):
    if name in students:
        total = 0
        print(f"{name}:")
        completed = len(students[name])
        print(" no " if completed == 0 else f" {completed} ", end="")
        print("completed courses", end="")
        print(":" if completed > 0 else "")
        for course in students[name]:
            total += course[1]
            print(f"  {course[0]} {course[1]}")
        if len(students[name]) != 0:
            print(f"average grade {total / len(students[name])}")
    else:
        print(f"{name}: no such person in the database")


def get_course_grade(students: dict, name: str, course: tuple):
    for student_course in students[name]:
        if student_course[0] == course[0]:
            return student_course[1]
    return -1


def add_course(students: dict, name: str, course: tuple):
    if course[1] == 0:  # courses with grade 0 should be ignored
        return
    course_grade = get_course_grade(students, name, course)
    if course_grade == -1:
        students[name].append(course)
    else:
        for i, student_course in enumerate(students[name]):
            if student_course[0] == course[0] and course_grade < course[1]:
                students[name][i] = course
                break


def get_average_grade(courses: list):
    total = 0
    for _, grade in courses:
        total += grade
    return total / len(courses)


def summary(students: dict):
    print("students", len(students))
    completed = 0
    found_name = ""
    for name, courses in students.items():
        if len(courses) > completed:
            found_name = name
            completed = len(courses)
    print(f"most courses completed {completed} {found_name}")
    best_average = 0
    for name in students:
        if get_average_grade(students[name]) > best_average:
            best_average = get_average_grade(students[name])
            found_name = name
    print(f"best average grade {best_average} {found_name}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 5))
    print_student(students, "Peter")
