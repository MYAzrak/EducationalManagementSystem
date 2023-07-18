from course import Course
from home_work import HomeWork


class Student:
    stus_accounts = {"mya": "1"}  # {'username': 'password'}

    @classmethod
    def get_stus_usernames(cls):
        return cls.stus_accounts.keys()

    @classmethod
    def get_stu_password(cls, username):
        return cls.stus_accounts.get(username)

    @classmethod
    def update_stus_accounts(cls, username, password):
        cls.stus_accounts.update({username: password})

    def __init__(self, username, password, full_name="None", email="None"):
        self.__username = username
        self.__password = password
        self.__full_name = full_name
        self.__email = email
        self.__registered_courses = []
        # Fills __registered_courses[] from the registered_students{} from the Course class
        for course_name in Course.registered_students.keys():
            if self.__username in Course.registered_students.get(course_name):
                self.__registered_courses.append(course_name)

    def register_in_course(self):
        """
        Gives a list of all courses for students
        to register from.
        """
        print("\nAvailable courses:")
        for course_name in Course.get_all_courses:
            print(course_name)

        course_name = input(
            "\nPlease enter the name of the course that you want to register in: (Type 'B' to go back)\n"
        )

        # Go back
        if course_name == "B" or course_name == "b":
            self.stu_menu()

        while (  # 1st condition: Unavailable course 2nd: Student already registered
            course_name not in Course.courses_details.keys()
            or course_name in self.__registered_courses
        ):
            course_name = input(
                "\nCourse unavailable or you are already registered in that course. Please write again: (Type 'B' to go back)\n"
            )
            if course_name == "B" or course_name == "b":
                self.stu_menu()

        self.__registered_courses.append(course_name)
        Course.add_student(self.__username, course_name)
        print("Course registered successfully!")
        self.stu_menu()

    def list_my_courses(self, from_menu=True):
        """
        Lists student's courses with their codes
        Used in the view_course() function
        """
        if len(self.__registered_courses) == 0:
            print("You are not registered in any course")
        else:
            print("My courses list:")
            for course_num, course_name in enumerate(self.__registered_courses, 1):
                print(
                    f"{course_num}- {course_name} ({Course.get_course_code(course_name)})"
                )

        if from_menu:  # If the function call was from the students' menu
            self.stu_menu()
        return len(self.__registered_courses)

    def view_course_details(self, course_num):
        """
        Used in the view_course() function
        List a course details such as, course name and code and taught by whom,
        courses assignments and their grades
        """
        course_name = self.__registered_courses[int(course_num) - 1]
        course_code = Course.get_course_code(course_name)
        course_prof = Course.get_course_prof(course_name)
        print(f"\n{course_name} ({course_code}) is taught by Prof.{course_prof}\n")
        print("Course assignments: ")
        for hw_num, grade in enumerate(
            HomeWork.allStudentsGrades[self.__username][course_name], 1
        ):
            print(f"HW #{hw_num} grade: {grade}/50")

    def deleteCourse(self, courseNum):
        """
        Used in the viewACourse() function
        Deletes a student's course
        """
        courseName = self.__registered_courses[int(courseNum) - 1]
        for (
            studentGrades
        ) in Course.allStudentsGrades.values():  # Removes all course's HWs grades
            if courseName in studentGrades:
                del studentGrades[courseName]

        Course.registered_students[courseName] = [
            student
            for student in Course.registered_students[courseName]
            if student != self.__username
        ]  # Removes the course from the Course class attribute

        self.__registered_courses.remove(
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
    def view_course(self):
        """
        View a summary of the course (name, code, professor, HWs)
        Delete a course
        View HWs grades
        Submit a solution
        """
        coursesNum = self.list_my_courses(False)
        if coursesNum == 0:
            print("You are not registered in any course")
            self.stu_menu()
        else:
            courseNum = input("Which ith course to view? ")
            optionsList = [str(x) for x in range(1, coursesNum + 1)]
            while courseNum not in optionsList:
                courseNum = input("Wrong input ")

            self.view_course_details(courseNum)

            option = input(
                "\nPlease make a choice: \n1- Unregister from the course\n2- Submit a HW\n3- Back\n"
            )
            while option not in ["1", "2", "3"]:
                option = input("Wrong input ")

            # Delete a course
            if option == "1":
                self.deleteCourse(courseNum)
                self.stu_menu()

            # Submit a solution
            elif option == "2":
                self.submitSolution(courseNum)

            # Go back
            elif option == "3":
                self.stu_menu()

    # Grades report(List of courses with # of HWs of each course and the total
    # grades, E.g. Course code CS333 - Total 4 HWs - Grade 101 / 200)
    def print_grade_report(self):
        for course, grades in HomeWork.allStudentsGrades.get(
            self.__username, {}
        ).items():
            numOfHWs = len(grades)
            totalGrade = sum(int(grade) for grade in grades if grade.isdigit())
            print(
                f"{course} has {numOfHWs} assignments - Total Grade: {totalGrade}/{numOfHWs * 50}"
            )

    def stu_menu(self):
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
            self.register_in_course()

        # List all student's courses
        elif option == "2":
            self.list_my_courses()

        # View a course details
        elif option == "3":
            self.view_course()

        # Print student's grade report
        elif option == "4":
            self.print_grade_report()

        # Back to main menu
        elif option == "5":
            del self



# line 92