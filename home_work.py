# Modules imported
import json


# Class definition
class HomeWork:
    # {'Course name' : ['HW names']}
    all_hws = {
        "Prog": ["HW1", "HW2"],
        "Prog2": [],
    }

    # {'student name' : {'course name' : ['HW1 grade' 'HW2 grade' ...] }}
    all_students_grades = {"mya": {"Prog": ["24", "NA"]}}

    # {'student name' : {'course name' : ['HW1 solution' 'HW2 solution' ...] }}
    all_students_submissions = {"mya": {"Prog": ["NA", "This is my solution"]}}

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

    def __init__(self, course_name: str, hw_name: str):
        self.__course_name = course_name  # Which course does it belong to
        self.__hw_name = hw_name  # The name of the HW
