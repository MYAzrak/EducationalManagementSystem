from main import main


class Student:
    stusAccounts = {}

    @staticmethod
    def stuMenu(user):
        # Student menu
        option = input(
            "Please make your choice:\n1. Register in a course\n2. List my courses\n3. View a course\n4. Grades report\n5. Log out"
        ).strip()

        # Wrong Input
        while option not in ["1", "2", "3", "4", "5"]:
            option = input("Wrong input\n")

        # Register in a course
        if option == "1":
            user.registerInCourse()

        # List all student's courses
        elif option == "2":
            user.listAllCourses()

        # View a course details
        elif option == "3":
            user.viewACourse()

        # Print student's grade report
        elif option == "4":
            user.printGradeReport()

        # Back to main menu
        elif option == "5":
            del user
            main()

    def __init__(self, username, password, fullName, email="None"):
        self.__username = username
        self.__password = password
        self.__fullName = fullName
        self.__email = email
        Student.stusAccounts.update({f"{username}": f"{password}"})
        print(f"Welcome {self.__fullName}!\n")

    # Register in a course (Gives a list of non-registered courses)
    def registerInCourse(self):
        pass

    # List my courses
    def listAllCourses(self):
        pass

    # View a course (summary of course name, code, list HW report
    # (Which HW did I submit ? , all grades, submit HW solution, unregister from
    # course)
    def viewACourse(self):
        pass

    # Grades report(List of courses with # of HWs of each course and the total
    # grades, E.g. Course code CS333 - Total 4 HWs - Grade 101 / 200)
    def printGradeReport(self):
        pass
