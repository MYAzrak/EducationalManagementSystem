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
        cls.registered_students[course_name].append(stu_name)

    @classmethod
    def create_course(cls, prof_name, course_name, course_code, tas):
        cls.courses_details[course_name] = [prof_name, course_code]
        cls.courses_tas[course_name] = tas
        cls.registered_students[course_name] = []

    @classmethod
    def print_all_students(cls, course_name) -> bool:
        '''
        Prints all students for a specific course
        Return false if the course does not have any registered students
        '''
        if cls.registered_students[course_name] == []:
            print("This course does not have any registered students")
            return False
        else:
            for student in cls.registered_students[course_name]:
                print(f"1- {student}")
                return True

    def __init__(self, name, code):
        self.__name = name
        self.__code = code
        # add to all_courses and registered_students when making a new course by prof
