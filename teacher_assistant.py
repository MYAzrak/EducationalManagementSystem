# Modules imported
import json
import os
from course import Course


# Class definition
class TeacherAssistant:
    tas_accounts = {}  # {'username': 'password'}

    @classmethod
    def get_tas_usernames(cls) -> dict:
        return cls.tas_accounts.keys()

    @classmethod
    def get_ta_password(cls, username: str) -> str:
        return cls.tas_accounts.get(username)

    @classmethod
    def register_ta(cls, username: str, password: str):
        cls.tas_accounts.update({username: password})

    @classmethod
    def save_json_files(cls):
        """
        Saves the data of tas_accounts{} to the json file
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            current_directory, r"LastSessionData\tas_accounts.json"
        )
        with open(file_path, "w") as f:
            json.dump(cls.tas_accounts, f)

    @classmethod
    def load_json_files(cls):
        """
        Loads the data of tas_accounts{} from the json file
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            current_directory, r"LastSessionData\tas_accounts.json"
        )
        with open(file_path, "r") as f:
            cls.tas_accounts = json.load(f)

    def __init__(self, username: str, password: str, fullName="None", email="None"):
        self.__username = username
        self.__password = password
        self.__fullName = fullName
        self.__email = email
        self.__registered_courses = []

        # Fills __registered_courses[] from the courses_tas{} from the Course class
        for course_name in Course.courses_tas.keys():
            if self.__username in Course.courses_tas[course_name]:
                self.__registered_courses.append(course_name)

    def view_courses(self):
        """
        Prints all the courses that the ta is registered to
        in order to assist the professor
        """
        if self.__registered_courses == []:
            print("You are not registered to any course")
            self.ta_menu()

        print("You are registered to these courses:")
        for course in self.__registered_courses:
            print(f"{course}")

    def ta_menu(self):
        # Teacher Assistant menu
        temp = input("Welcome to the Teacher Assistants menu!\n")

        option = input(
            "Please make your choice:\n1. View my courses\n2. Log out\n"
        ).strip()

        # Wrong Input
        while option not in ["1", "2"]:
            option = input("Wrong input\n").strip()

        # View courses
        if option == "1":
            self.view_courses()
            self.ta_menu()

        # Back to main menu
        elif option == "2":
            del self
