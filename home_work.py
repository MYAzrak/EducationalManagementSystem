# Modules imported
import json
import os


# Class definition
class HomeWork:
    # {'Course name' : ['HW names']}
    all_hws = {}

    # {'student name' : {'course name' : ['HW1 grade' 'HW2 grade' ...] }}
    all_students_grades = {}

    # {'student name' : {'course name' : ['HW1 solution' 'HW2 solution' ...] }}
    all_students_submissions = {}

    @classmethod
    def get_student_course_grades(cls, course_name: str, student_name: str) -> list:
        return cls.all_students_grades[student_name][course_name]

    @classmethod
    def set_student_hw_grade(
        cls, course_name: str, hw_name: str, student_name: str, hw_grade: str
    ):
        """
        Sets a grade for a hw in a course for a student
        """
        hw_num = cls.all_hws[course_name].index(hw_name)
        cls.all_students_grades[student_name][course_name][hw_num] = hw_grade

    @classmethod
    def get_student_hw_solution(
        cls, course_name: str, hw_name: str, student_name: str
    ) -> str:
        """
        Returns a student's solution of a course hw
        """
        hw_num = cls.all_hws[course_name].index(hw_name)
        return cls.all_students_submissions[student_name][course_name][hw_num]

    @classmethod
    def save_json_files(cls):
        """
        Saves the data of all_hws{}, all_students_grades{}, and all_students_submissions{} to the json file
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, r"LastSessionData\all_hws.json")
        with open(file_path, "w") as f:
            json.dump(cls.all_hws, f)

        file_path = os.path.join(
            current_directory, r"LastSessionData\all_students_grades.json"
        )
        with open(file_path, "w") as f:
            json.dump(cls.all_students_grades, f)

        file_path = os.path.join(
            current_directory, r"LastSessionData\all_students_submissions.json"
        )
        with open(file_path, "w") as f:
            json.dump(cls.all_students_submissions, f)

    @classmethod
    def load_json_files(cls):
        """
        Loads the data to all_hws{}, all_students_grades{}, and all_students_submissions{} from the json file
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, r"LastSessionData\all_hws.json")
        with open(file_path, "r") as f:
            cls.all_hws = json.load(f)

        file_path = os.path.join(
            current_directory, r"LastSessionData\all_students_grades.json"
        )
        with open(file_path, "r") as f:
            cls.all_students_grades = json.load(f)

        file_path = os.path.join(
            current_directory, r"LastSessionData\all_students_submissions.json"
        )
        with open(file_path, "r") as f:
            cls.all_students_submissions = json.load(f)

    def __init__(self, course_name: str, hw_name: str):
        self.__course_name = course_name  # Which course does it belong to
        self.__hw_name = hw_name  # The name of the HW
