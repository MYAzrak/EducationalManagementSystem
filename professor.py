from course import Course
from home_work import HomeWork
from teacher_assistant import TeacherAssistant


class Professor:
    # {'username': password}
    profs_accounts = {"ali": "1"}

    @classmethod
    def get_profs_usernames(cls):
        return cls.profs_accounts.keys()

    @classmethod
    def get_prof_password(cls, username):
        return cls.profs_accounts.get(username)

    @classmethod
    def update_profs_accounts(cls, username, password):
        cls.profs_accounts.update({username: password})

    def __init__(self, username, password, full_name="None", email="None"):
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
        while course_name in Course.get_all_courses():
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
        Used in the show_course_details function
        Lists the hws of a single course for a professor
        """
        for hw_num, hw in enumerate(HomeWork.all_hws[course_name], 1):
            print(f"{hw_num}- {hw}")

    def create_hw(self, course_name: str):
        hw_name = input("\nWhat would you like to name the assignment? ").strip()
        while hw_name in HomeWork.all_hws[course_name]:
            hw_name = input("\nYou already have this assignment: ").strip()

        # Updates the all_hws dictionary
        HomeWork.all_hws[course_name].append(hw_name)

        # Updates the all_students_grades dictionary
        for student in HomeWork.all_students_grades.keys():
            for course in student.keys():
                if course == course_name:
                    HomeWork.all_students_grades[student][course].append("NA")

        # Updates the all_students_submissions dictionary
        for student in HomeWork.all_students_submissions.keys():
            for course in student.keys():
                if course == course_name:
                    HomeWork.all_students_submissions[student][course].append("NA")

        print("Homework created successfully!")

    def view_hw(self, course_name):
        pass

    def show_course_details(self):
        """
        View HW (Show info, show grades report, list solutions, view solution (show info, set grade, set a comment, go back), Go back (== log out) ), Go back (== log out) )
        """
        print("Your list of courses:")
        self.list_my_courses(False)

        course_name = input("Which course do you want to view? ").strip()
        while course_name not in self.__created_courses:
            course_name = input("You do not have such course: ").strip()

        option = input(
            "\nChoose an option:\n1- List HWs\n2- Create a HW\n3- View a HW\n4- Back\n"
        )

        while option not in ["1", "2", "3", "4"]:
            option = input("Wrong input: ")

        if option == "1":
            self.list_hws(course_name)
            self.prof_menu()

        elif option == "2":
            self.create_hw(course_name)
            self.prof_menu()

        elif option == "3":
            self.view_hw(course_name)
            self.prof_menu()

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
