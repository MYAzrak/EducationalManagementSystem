# Modules imported
from home_work import HomeWork


# Class definition
class Course:
    # {'Course name' : ['Course professor', 'Course code']}
    courses_details = {
        "Prog": ["ali", "123"],
        "Prog2": ["Yaser", "321"],
        "MTH": ["ali", "789"],
    }

    # {'Course name' : ['TA1', 'TA2', ...]}
    courses_tas = {
        "Prog": ["Mohammad", "Yaser"],
        "Prog2": ["Mohammad", "Yaser"],
    }

    # {'Course name' : [list of students names]]}
    registered_students = {
        "Prog": ["mya"],
        "Prog2": [],
    }

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
        if cls.registered_students[course_name] == []:
            print("This course does not have any registered students")
            return False
        else:
            for student in cls.registered_students[course_name]:
                print(f"1- {student}")
                return True

    def __init__(self, name: str, code: str):
        self.__name = name
        self.__code = code
