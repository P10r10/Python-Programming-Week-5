# First write a function named add_student, which adds a new student to the
# database. Also write a preliminary version of the function print_student,
# which prints out the information of a single student.
# After that write a function named add_course, which adds a completed
# course to the information of a specific student in the database. The course
# data is a tuple consisting of the name of the course and the grade

def add_student(students: dict, name: str):
    students[name] = []


def print_student(students: dict, name: str):
    if name in students:
        total = 0
        print(f"{name}:")
        print(f" {len(students[name])} completed courses:")
        for course in students[name]:
            total += course[1]
            print(f"  {course[0]} {course[1]}")
        if len(students[name]) != 0:
            print(f"average grade {total / len(students[name])}")
    else:
        print(f"{name}: no such person in the database")


# def is_course_in_database(students: dict, name: str, course: tuple):
#     for student_course in students[name]:
#         if course[0] == student_course[0]:
#             return True
#     return False


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
                print(students[name][i])
                students[name][i] = course
                break


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")
