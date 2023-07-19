class HomeWork:
    # {'Course name' : ['HW numbers']}
    all_hws = {
        "Prog": ["HW1", "HW2"],
        "Prog2": [],
    }

    # {'student name' : {'course name' : ['HW1 grade' 'HW2 grade' ...] }}
    all_students_grades = {"mya": {"Prog": ["24", "NA"]}}

    # {'student name' : {'course name' : ['HW1 solution' 'HW2 solution' ...] }}
    all_students_submissions = {"mya": {"Prog": ["None", "This is my solution"]}}

    @classmethod
    def get_student_course_grades(cls, course_name, username):
        return cls.all_students_grades[username][course_name]

    def __init__(self, course_name, hw_name):
        self.__course_name = course_name  # Which course does it belong to
        self.__hw_name = hw_name  # The name of the HW
        # add to allHWs when making a new HW by prof
