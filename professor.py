# Modules imported
import json
import os
from course import Course
from home_work import HomeWork
from teacher_assistant import TeacherAssistant


# Class definition
class Professor:
    # {'username': 'password'}
    profs_accounts = {}

    @classmethod
    def get_profs_usernames(cls) -> dict:
        return cls.profs_accounts.keys()

    @classmethod
    def get_prof_password(cls, username: str) -> str:
        return cls.profs_accounts.get(username)

    @classmethod
    def register_prof(cls, username: str, password: str):
        cls.profs_accounts.update({username: password})

    @classmethod
    def save_json_files(cls):
        """
        Saves the data of profs_accounts{} to the json file
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            current_directory, r"LastSessionData\profs_accounts.json"
        )
        with open(file_path, "w") as f:
            json.dump(cls.profs_accounts, f)

    @classmethod
    def load_json_files(cls):
        """
        Loads the data of profs_accounts{} from the json file
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            current_directory, r"LastSessionData\profs_accounts.json"
        )
        with open(file_path, "r") as f:
            cls.profs_accounts = json.load(f)

    def __init__(self, username: str, password: str, full_name="None", email="None"):
        self.__username = username
        self.__password = password
        self.__full_name = full_name
        self.__email = email
        self.__created_courses = []

        # Fills __created_courses[] from the courses_details{} from the Course class
        for course_name in Course.courses_details.keys():
            if self.__username in Course.courses_details.get(course_name):
                self.__created_courses.append(course_name)

    def list_my_courses(self, from_menu=True):
        """
        Lists the courses created by the professor
        """
        if self.__created_courses == []:
            print("You do not have any course\n")
            self.prof_menu()

        for course_name in self.__created_courses:
            print(f"- {course_name} ({Course.get_course_code(course_name)})")

        if from_menu:
            self.prof_menu()

    def create_course(self):
        course_name = input("What would you like to name your course? ").strip()
        while course_name in Course.get_all_avail_courses():
            course_name = input(
                "This course exists already. Please choose another name: ('B' to go back) "
            ).strip()
            if course_name == "B" or course_name == "b":
                self.prof_menu()

        with_ta = input("Would you like to have any teacher assistants? (Y/N) ").strip()
        tas = []

        # The professor wants to have TAs with them in the course
        if with_ta == "y" or with_ta == "Y":
            ta = input("Enter the TA name: ")
            tas.append(ta)
            while ta != "N" and ta != "n":
                ta = input("Do you want to add another TA? ('N' if no)")
                if ta != "n" or ta != "N":
                    tas.append(ta)

        course_code = input("What would you like your course code to be? ").strip()
        Course.create_course(self.__username, course_name, course_code, tas)
        self.__created_courses.append(course_name)
        print("Course created successfully!\n")
        self.prof_menu()

    def list_hws(self, course_name: str):
        """
        Used in the show_course_details and view_hw functions
        Lists the hws of a single course for a professor
        """
        if HomeWork.all_hws[course_name] == []:
            print("This course does not have any homeworks\n")
            self.show_course_details()
        else:
            for hw_num, hw in enumerate(HomeWork.all_hws[course_name], 1):
                print(f"{hw_num}- {hw}")

    def create_hw(self, course_name: str):
        hw_name = input("\nWhat would you like to name the assignment? ").strip()
        while hw_name in HomeWork.all_hws[course_name]:
            hw_name = input("\nYou already have this assignment: ").strip()

        # Updates the all_hws{}
        HomeWork.all_hws[course_name].append(hw_name)

        # Updates the all_students_grades{}
        for student in HomeWork.all_students_grades.keys():
            for course in HomeWork.all_students_grades[student].keys():
                if course == course_name:
                    HomeWork.all_students_grades[student][course].append("NA")

        # Updates the all_students_submissions{}
        for student in HomeWork.all_students_submissions.keys():
            for course in HomeWork.all_students_grades[student].keys():
                if course == course_name:
                    HomeWork.all_students_submissions[student][course].append("NA")

        print("Homework created successfully!")

    def view_solution(self, course_name: str, hw_name: str):
        """
        Used in the view_hw function
        View a student's solution for a hw
        """
        has_students = Course.print_all_students(course_name)

        # If the course does not have any students
        if not has_students:
            self.view_hw()

        student_name = input(
            "Which student do you want to view their solution? "
        ).strip()
        while student_name not in Course.registered_students[course_name]:
            student_name = input("This students does not exist: ").strip()

        hw_solution = HomeWork.get_student_hw_solution(
            course_name, hw_name, student_name
        )
        print(hw_solution)
        self.view_hw(course_name)

    def set_grade(self, course_name: str, hw_name: str):
        """
        Used in the view_hw function
        Set a student's grade for a hw
        """
        has_students = Course.print_all_students(course_name)

        # If the course does not have any students
        if not has_students:
            self.prof_menu()

        student_name = input("Which student to set their grade? ").strip()
        while student_name not in Course.registered_students[course_name]:
            student_name = input("This students does not exist: ").strip()

        hw_grade = input("Input the grade: ").strip()
        HomeWork.set_student_hw_grade(course_name, hw_name, student_name, hw_grade)

        print(f"Grade changed successfully!\n")
        self.view_hw(course_name)

    def view_hw(
        self,
        course_name: str,
    ):
        """
        Used in the show_course_details function
        Shows info about professors' homeworks
        View a solution, set a grade
        """
        self.list_hws(course_name)
        hw_name = input("Which assignment would you like to view? ").strip()
        while hw_name not in HomeWork.all_hws[course_name]:
            hw_name = input("Homework not found: ").strip()

        option = input(
            "Choose your option\n1- View a solution\n2- Set a grade\n3- Back\n"
        ).strip()

        # Wrong input
        while option not in ["1", "2", "3"]:
            option = input("Wrong input: ").strip()

        # View a solution
        if option == "1":
            self.view_solution(course_name, hw_name)

        # Set a grade
        elif option == "2":
            self.set_grade(course_name, hw_name)

        # Back
        elif option == "3":
            self.show_course_details()

    def show_course_details(self):
        """
        Used in the prof_menu()
        """
        print("\nYour list of courses:")
        self.list_my_courses(False)

        course_name = input("Which course do you want to view? ").strip()
        while course_name not in self.__created_courses:
            course_name = input("You do not have such course: ").strip()

        option = input(
            "\nChoose an option:\n1- List HWs\n2- Create a HW\n3- View a HW\n4- Back\n"
        )

        while option not in ["1", "2", "3", "4"]:
            option = input("Wrong input: ")

        # List HWs
        if option == "1":
            self.list_hws(course_name)
            self.show_course_details()

        # Create a HW
        elif option == "2":
            self.create_hw(course_name)
            self.show_course_details()

        # View a HW
        elif option == "3":
            self.view_hw(course_name)
            self.show_course_details()

        # Back
        elif option == "4":
            self.prof_menu()

    def prof_menu(self):
        # Professor menu
        temp = input("\nWelcome to the Professors menu!\n")

        option = input(
            "Please make your choice:\n1. List my courses\n2. Create a course\n3. View a course\n4. Log out\n"
        ).strip()

        # Wrong Input
        while option not in ["1", "2", "3", "4"]:
            option = input("Wrong input\n")

        # List prof courses
        if option == "1":
            self.list_my_courses()

        # Create a course
        elif option == "2":
            self.create_course()

        # View a course details
        elif option == "3":
            self.show_course_details()

        # Back to main menu
        elif option == "4":
            del self
