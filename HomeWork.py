class HomeWork:
    allHWs = {
        "Prog": ["HW1", "HW2"],
        "Prog2": [],
    }  # {'Course name' : ['HW numbers']}

    allStudentsGrades = {
        "mya": {"Prog": ["24", "NA"]}
    }  # {'student name' : {'course name' : ['HW1 grade' 'HW2 grade' ...] }}

    allStudentsSubmissions = {
        "mya": {"Prog": ["None", "This is my solution"]}
    }  # {'student name' : {'course name' : ['HW1 solution' 'HW2 solution' ...] }}

    def __init__(self, courseName, HWName):
        self.__courseName = courseName  # Which course does it belong to
        self.__HWName = HWName  # The name of the HW
        # add to allHWs when making a new HW by prof
