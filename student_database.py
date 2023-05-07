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
        print(f"average grade {total / len(students[name])}")
    else:
        print(f"{name}: no such person in the database")


def get_grade(students: dict, name: str, course: tuple):
    for xx in students[name]:

def add_course(students: dict, name: str, course: tuple):
    if course[1] == 0:  # courses with grade 0 should be ignored
        return
    students[name].append(course)
            # if len(students[name]) == 0: # students without course will add one
    #     students[name].append(course)
    # else:
    #     for crs in students[name]:
    #         None
            # print("crs", crs[0], crs[1])
            # if crs[0] == course[0] and crs[1] < course[1]:
            #     students[name].append(course)


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    # print_student(students, "Peter")
    for a in students["Peter"]: # lists all Peter's courses
        print(a)
    lst = []
