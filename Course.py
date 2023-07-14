class Course:
    allCourses = {"Prog": "123", "Prog2": "321"}  # {'Course name' : 'Course code'}
    registeredStudents = {
        "Prog": ["mya"],
        "Prog2": [],
    }  # {'Course name' : [list of students names]]}

    def __init__(self, name, code):
        self.__name = name
        self.__code = code
