from main import main


class Student:
    stusAccounts = {}

    def __init__(
        self, username, password, fullName="None", email="None", registeredCourses=[]
    ):
        self.__username = username
        self.__password = password
        self.__fullName = fullName
        self.__email = email
        self.__registeredCourses = registeredCourses

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

    def stuMenu(self):
        # Student menu
        temp = input("Welcome to the Students menu!\n")
        
        option = input(
            "Please make your choice:\n1. Register in a course\n2. List my courses\n3. View a course\n4. Grades report\n5. Log out"
        ).strip()

        # Wrong Input
        while option not in ["1", "2", "3", "4", "5"]:
            option = input("Wrong input\n")

        # Register in a course
        if option == "1":
            self.registerInCourse()

        # List all student's courses
        elif option == "2":
            self.listAllCourses()

        # View a course details
        elif option == "3":
            self.viewACourse()

        # Print student's grade report
        elif option == "4":
            self.printGradeReport()

        # Back to main menu
        elif option == "5":
            del self
            main()
