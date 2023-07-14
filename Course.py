class Course:
    listOfCourses = {}

    def __init__(self, name, code, registeredStudents=[]):
        self.__name = name
        self.__code = code
        self.__registeredStudents = registeredStudents
