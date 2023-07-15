class Course:
    allCourses = {
        "Prog": ["Ali", "123"],
        "Prog2": ["Yaser", "321"],
    }  # {'Course name' : ['Course professor', 'Course code']}

    registeredStudents = {
        "Prog": ["mya"],
        "Prog2": [],
    }  # {'Course name' : [list of students names]]}

    def __init__(self, name, code):
        self.__name = name
        self.__code = code
        # add to allCourses and registeredStudents when making a new course by prof
