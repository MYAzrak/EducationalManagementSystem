from Course import Course
from HomeWork import HomeWork


class Student:
    stusAccounts = {"mya": "1"}  # {'username': 'password'}

    def __init__(self, username, password, fullName="None", email="None"):
        self.__username = username
        self.__password = password
        self.__fullName = fullName
        self.__email = email
        self.__registeredCourses = []
        for (
            courseName
        ) in (
            Course.registeredStudents.keys()
        ):  # Fills __registeredCourses[] from the registeredStudents{} from the Course class
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

        # Go back
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

    def listMyCourses(self, fromMenu=True):
        """
        Lists student's courses with their codes
        Used in the viewACourse() function
        """
        if len(self.__registeredCourses) == 0:
            print("You are not registered in any course")
        else:
            print("My courses list:")
            for courseNum, course in enumerate(self.__registeredCourses, 1):
                print(f"{courseNum}- {course} ({Course.allCourses.get(course)[1]})")

        if fromMenu:  # If the function call was from the students menu
            self.stuMenu()
        return len(self.__registeredCourses)

    def viewCourseDetails(self, courseNum):
        """
        Used in the viewACourse() function
        List a course details such as, course name and code and taught by whom,
        courses assignments and their grades
        """
        courseName = self.__registeredCourses[int(courseNum) - 1]
        courseCode = Course.allCourses.get(courseName)[1]
        courseProfessor = Course.allCourses.get(courseName)[0]
        print(f"\n{courseName} ({courseCode}) is taught by Prof.{courseProfessor}\n")
        print("Course assignments: ")
        for HWNum, grade in enumerate(
            HomeWork.allStudentsGrades[self.__username][courseName], 1
        ):
            print(f"HW #{HWNum} grade: {grade}/50")

    def deleteCourse(self, courseNum):
        """
        Used in the viewACourse() function
        Deletes a student's course
        """
        courseName = self.__registeredCourses[int(courseNum) - 1]
        for (
            studentGrades
        ) in Course.allStudentsGrades.values():  # Removes all course's HWs grades
            if courseName in studentGrades:
                del studentGrades[courseName]

        Course.registeredStudents[courseName] = [
            student
            for student in Course.registeredStudents[courseName]
            if student != self.__username
        ]  # Removes the course from the Course class attribute

        self.__registeredCourses.remove(
            courseName
        )  # Removes the course from the instance attribute

    def submitSolution(self, courseNum):
        """
        Used in the viewACourse() function
        Submits a student's course HW solution
        """
        pass

    # View a course (summary of course name, code, list HW report
    # (Which HW did I submit ? , all grades, submit HW solution, unregister from
    # course)
    def viewACourse(self):
        """
        View a summary of the course (name, code, professor, HWs)
        Delete a course
        View HWs grades
        Submit a solution
        """
        coursesNum = self.listMyCourses(False)
        if coursesNum == 0:
            print("You are not registered in any course")
            self.stuMenu()
        else:
            courseNum = input("Which ith course to view? ")
            optionsList = [str(x) for x in range(1, coursesNum + 1)]
            while courseNum not in optionsList:
                courseNum = input("Wrong input ")

            self.viewCourseDetails(courseNum)

            option = input(
                "\nPlease make a choice: \n1- Unregister from the course\n2- Submit a HW\n3- Back\n"
            )
            while option not in ["1", "2", "3"]:
                option = input("Wrong input ")

            # Delete a course
            if option == "1":
                self.deleteCourse(courseNum)
                self.stuMenu()

            # Submit a solution
            elif option == "2":
                self.submitSolution(courseNum)

            # Go back
            elif option == "3":
                self.stuMenu()

    # Grades report(List of courses with # of HWs of each course and the total
    # grades, E.g. Course code CS333 - Total 4 HWs - Grade 101 / 200)
    def printGradeReport(self):
        for course, grades in HomeWork.allStudentsGrades.get(self.__username, {}).items():
            numOfHWs = len(grades)
            totalGrade = sum(int(grade) for grade in grades if grade.isdigit())
            print(f"{course} has {numOfHWs} assignments - Total Grade: {totalGrade}/{numOfHWs * 50}")

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
            self.listMyCourses()

        # View a course details
        elif option == "3":
            self.viewACourse()

        # Print student's grade report
        elif option == "4":
            self.printGradeReport()

        # Back to main menu
        elif option == "5":
            del self
