# Modules imported
import json
import os
from home_work import HomeWork


# Class definition
class Course:
    # {'Course name' : ['Course professor', 'Course code']}
    courses_details = {}

    # {'Course name' : ['TA1', 'TA2', ...]}
    courses_tas = {}

    # {'Course name' : [list of students names]]}
    registered_students = {}

    @classmethod
    def get_all_avail_courses(cls) -> dict:
        return cls.courses_details.keys()

    @classmethod
    def get_course_prof(cls, course_name) -> str:
        return cls.courses_details.get(course_name)[0]

    @classmethod
    def get_course_code(cls, course_name) -> str:
        return cls.courses_details.get(course_name)[1]

    @classmethod
    def add_student_to_course(cls, stu_name: str, course_name: str):
        """
        Adds a student to a specific course
        Updates registered_students{}, all_students_grades{} and all_students_submissions{}
        """
        cls.registered_students[course_name].append(stu_name)
        HomeWork.all_students_grades[stu_name].update({course_name: []})
        HomeWork.all_students_submissions[stu_name].update({course_name: []})

    @classmethod
    def create_course(
        cls, prof_name: str, course_name: str, course_code: str, tas: list
    ):
        """
        Updates courses_details{}, courses_tas{}, registered_students{}, and all_hws{}
        """
        cls.courses_details[course_name] = [prof_name, course_code]
        cls.courses_tas[course_name] = tas
        cls.registered_students[course_name] = []
        HomeWork.all_hws[course_name] = []

    @classmethod
    def print_all_students(cls, course_name: str) -> bool:
        """
        Prints all students for a specific course
        Return false if the course does not have any registered students
        """
        students = cls.registered_students[course_name]

        if not students:
            print("This course does not have any registered students")
            return False
        else:
            for student in students:
                print(f"1- {student}")
            return True

    @classmethod
    def save_json_files(cls):
        """
        Saves the data of registered_students{}, courses_details{}, and courses_tas{} to the json file
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            current_directory, r"LastSessionData\registered_students.json"
        )
        with open(file_path, "w") as f:
            json.dump(cls.registered_students, f)

        file_path = os.path.join(
            current_directory, r"LastSessionData\courses_details.json"
        )
        with open(file_path, "w") as f:
            json.dump(cls.courses_details, f)

        file_path = os.path.join(current_directory, r"LastSessionData\courses_tas.json")
        with open(file_path, "w") as f:
            json.dump(cls.courses_tas, f)

    @classmethod
    def load_json_files(cls):
        """
        Loads the data to registered_students{}, courses_details{}, and courses_tas{} from the json file
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            current_directory, r"LastSessionData\tas_accounts.json"
        )
        with open(file_path, "r") as f:
            cls.tas_accounts = json.load(f)

        file_path = os.path.join(
            current_directory, r"LastSessionData\courses_details.json"
        )
        with open(file_path, "r") as f:
            cls.courses_details = json.load(f)

        file_path = os.path.join(current_directory, r"LastSessionData\courses_tas.json")
        with open(file_path, "r") as f:
            cls.courses_tas = json.load(f)

    def __init__(self, name: str, code: str):
        self.__name = name
        self.__code = code
