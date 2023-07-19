class Course:
    # {'Course name' : ['Course professor', 'Course code']}
    courses_details = {
        "Prog": ["Ali", "123"],
        "Prog2": ["Yaser", "321"],
        "MTH": ["Ali", "789"],
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
    def get_all_courses(cls):
        return cls.courses_details.keys()

    @classmethod
    def get_course_prof(cls, course_name):
        return cls.courses_details.get(course_name)[0]

    @classmethod
    def get_course_code(cls, course_name):
        return cls.courses_details.get(course_name)[1]

    @classmethod
    def add_student(cls, stu_name, course_name):
        """
        Adds a student to a specific course
        """
        cls.registered_students[course_name].extend([stu_name])

    @classmethod
    def create_course(cls, prof_name, course_name, course_code, tas):
        cls.courses_details[course_name] = [prof_name, course_code]
        cls.courses_tas[course_name] = tas

    def __init__(self, name, code):
        self.__name = name
        self.__code = code
        # add to all_courses and registered_students when making a new course by prof
