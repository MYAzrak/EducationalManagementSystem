# Modules imported
import json
import os
from course import Course
from home_work import HomeWork


# Class definition
class Student:
    # {'username': 'password'}
    stus_accounts = {}

    @classmethod
    def get_stus_usernames(cls) -> dict:
        """
        Returns all students' usernames
        """
        return cls.stus_accounts.keys()

    @classmethod
    def get_stu_password(cls, student_name: str) -> str:
        """
        Returns the password of a specific students username
        """
        return cls.stus_accounts.get(student_name)

    @classmethod
    def register_stu(cls, student_name: str, password: str):
        """
        Updates stus_accounts{} and adds a new username
        """
        cls.stus_accounts.update({student_name: password})

    @classmethod
    def load_json_files(cls):
        """
        Loads the data of stus_accounts{} from the json file
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            current_directory, "LastSessionData\stus_accounts.json"
        )

        with open(file_path, "r") as f:
            cls.stus_accounts = json.load(f)

    def __init__(self, username: str, password: str, full_name="None", email="None"):
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
        for course_name in Course.get_all_avail_courses():
            print(course_name)

        course_name = input(
            "\nPlease enter the name of the course that you want to register in: (Type 'B' to go back)\n"
        )

        # Go back
        if course_name == "B" or course_name == "b":
            self.stu_menu()

        # 1st condition: Unavailable course 2nd: Student already registered
        while (
            course_name not in Course.get_all_avail_courses()
            or course_name in self.__registered_courses
        ):
            course_name = input(
                "\nCourse unavailable or you are already registered in that course. Please write again: (Type 'B' to go back)\n"
            )
            if course_name == "B" or course_name == "b":
                self.stu_menu()

        # Adds the course to the __registered_courses[], registered_students{}, all_students_grades{} and all_students_submissions{}
        self.__registered_courses.append(course_name)
        Course.add_student_to_course(self.__username, course_name)
        print("Course registered successfully!\n")
        self.stu_menu()

    def list_my_courses(self, from_menu=True) -> int:
        """
        Lists student's courses with their codes
        Used in the view_course() function
        Returns the number of courses that the student is registered to
        """
        if len(self.__registered_courses) == 0:
            print("You are not registered in any course")
        else:
            print("My courses list:")
            for course_num, course_name in enumerate(self.__registered_courses, 1):
                print(
                    f"{course_num}- {course_name} ({Course.get_course_code(course_name)})"
                )
        print("\n")

        # If the function call was from the students' menu
        if from_menu:
            self.stu_menu()
        return len(self.__registered_courses)

    def view_course_details(self, course_num: int):
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
            HomeWork.get_student_course_grades(course_name, self.__username), 1
        ):
            print(f"HW #{hw_num} grade: {grade}/50")

    def unregister_from_course(self, course_num: int):
        """
        Used in the view_course() function
        Deletes a student from a course
        """
        course_name = self.__registered_courses[int(course_num) - 1]

        # Removes all course's HWs grades
        del HomeWork.all_students_grades[self.__username][course_name]

        # Remove all course's HWs submissions
        del HomeWork.all_students_submissions[self.__username][course_name]

        # Removes the course from the Course class attribute
        Course.registered_students[course_name] = [
            student
            for student in Course.registered_students[course_name]
            if student != self.__username
        ]

        # Removes the course from the instance attribute
        self.__registered_courses.remove(course_name)
        print(f"You are no longer registered to {course_name}")

    def submit_solution(self, course_num: int):
        """
        Used in the view_course() function
        Submits a student's course HW solution
        """
        course_name = self.__registered_courses[int(course_num) - 1]
        hws_num = len(HomeWork.all_students_submissions[self.__username][course_name])
        hw_number_input = input(
            f"Enter the HW number you want to submit (1 to {hws_num}): "
        )

        options_list = [str(x) for x in range(1, hws_num + 1)]
        # Check if the input is a valid HW number
        while hw_number_input not in options_list:
            hw_number_input = input("Invalid HW number: ")

        hw_solution_input = input("Enter your HW solution: ")

        # Update all_students_submissions{}
        HomeWork.all_students_submissions[self.__username][course_name][
            int(hw_number_input) - 1
        ] = hw_solution_input
        print("Submitted successfully!")
        self.stu_menu()

    def view_course(self):
        """
        View a summary of the course (name, code, professor, HWs)
        Delete a course
        View HWs grades
        Submit a solution
        """
        courses_num = self.list_my_courses(False)
        if courses_num == 0:
            print("You are not registered in any course")
            self.stu_menu()
        else:
            course_num = input("Which ith course to view? ")
            options_list = [str(x) for x in range(1, courses_num + 1)]
            while course_num not in options_list:
                course_num = input("Wrong input: ")

            self.view_course_details(course_num)

            option = input(
                "\nPlease make a choice: \n1- Unregister from the course\n2- Submit a HW\n3- Back\n"
            )
            while option not in ["1", "2", "3"]:
                option = input("Wrong input ")

            # Unregister from a course
            if option == "1":
                self.unregister_from_course(course_num)
                self.stu_menu()

            # Submit a solution
            elif option == "2":
                self.submit_solution(course_num)

            # Go back
            elif option == "3":
                self.stu_menu()

    def print_grade_report(self):
        """
        Grades report (List of courses with # of HWs of each course and the total)
        grades, E.g. Course code CS333 - Total 4 HWs - Grade 101 / 200)
        """
        for course, grades in HomeWork.all_students_grades.get(self.__username).items():
            hws_num = len(grades)
            total_grade = sum(int(grade) for grade in grades if grade.isdigit())
            print(
                f"{course} has {hws_num} assignments - Total Grade: {total_grade}/{hws_num * 50}"
            )

        self.stu_menu()

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
