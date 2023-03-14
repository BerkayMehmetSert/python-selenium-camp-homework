import constants

students = []


def add_student():
    name = input(constants.STUDENT_NAME)
    surname = input(constants.STUDENT_SURNAME)
    student = name + " " + surname
    students.append(student)
    print(constants.STUDENT_SUCCESS)


def add_multiple_students():
    number = int(input(constants.STUDENT_NUMBER))
    for _ in range(number):
        add_student()


def remove_student():
    name = input(constants.STUDENT_NAME)
    surname = input(constants.STUDENT_SURNAME)
    student = name + " " + surname
    if student in students:
        students.remove(student)
        print(constants.STUDENT_REMOVED)
    else:
        print(constants.STUDENT_NOT_FOUND)


def multiple_remove_student():
    number = int(input(constants.STUDENT_NUMBER))

    while number > 0:
        remove_student()
        number -= 1


def get_all_students():
    if len(students) != 0:
        for student in students:
            print(student)
    else:
        print(constants.STUDENT_LIST_EMPTY)


def search_student():
    name = input(constants.STUDENT_NAME)
    surname = input(constants.STUDENT_SURNAME)
    student = name + " " + surname

    print(students.index(student))


def show_menu():
    print(constants.MENU)

    choice = int(input(constants.CHOICE))

    while True:
        if choice == 1:
            add_student()
        elif choice == 2:
            add_multiple_students()
        elif choice == 3:
            remove_student()
        elif choice == 4:
            multiple_remove_student()
        elif choice == 5:
            get_all_students()
        elif choice == 6:
            search_student()
        elif choice == 7:
            print(constants.THANK_YOU_MESSAGE)
            exit()
        else:
            print(constants.CHOICE_INVALID)
        show_menu()


print(constants.WELCOME_MESSAGE)
show_menu()
