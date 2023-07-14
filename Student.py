from Course import Course


class Student:
    stusAccounts = {"mya": "1"}  # {'username': 'password'}

    def __init__(self, username, password, fullName="None", email="None"):
        self.__username = username
        self.__password = password
        self.__fullName = fullName
        self.__email = email
        self.__registeredCourses = []
        for courseName in Course.registeredStudents.keys():
            if self.__username in Course.registeredStudents.get(courseName):
                self.__registeredCourses.append(courseName)

    def registerInCourse(self):
        """
        Gives a list of all courses for students
        to register from.
        """
        print("\nAvailable courses:")
        for key in Course.allCourses.keys():
            print(key)

        courseName = input(
            "\nPlease enter the name of the course that you want to register in: (Type 'B' to go back)\n"
        )

        if courseName == "B" or courseName == "b":
            self.stuMenu()

        while (  # 1st condition: Unavailable course 2nd: Student already registered
            courseName not in Course.allCourses.keys()
            or courseName in self.__registeredCourses
        ):
            courseName = input(
                "\nCourse unavailable or you are already registered in that course. Please write again: (Type 'B' to go back)\n"
            )
            if courseName == "B" or courseName == "b":
                self.stuMenu()

        self.__registeredCourses.append(courseName)
        Course.registeredStudents[courseName].extend([self.__username])
        print("Course registered successfully!")
        self.stuMenu()

    def listAllCourses(self):
        """
        Lists student's courses with their codes
        """
        for course in self.__registeredCourses:
            print(f"- {course} : {Course.allCourses.get(course)}\n")
        self.stuMenu()

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
            "Please make your choice:\n1. Register in a course\n2. List my courses\n3. View a course\n4. Grades report\n5. Log out\n"
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
