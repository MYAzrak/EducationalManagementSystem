class Student:
    stusAccounts = {}

    @staticmethod
    def stuMenu():
        test = input("Student menu!")
        """
        Register in a course (Gives a list of non-registered courses)
        List my courses

        View a course (summary of course name, code, list HW report
        (Which HW did I submit ? , all grades, submit HW solution, unregister from
        course)

        Grades report(List of courses with # of HWs of each course and the total
        grades, E.g. Course code CS333 - Total 4 HWs - Grade 101 / 200)

        Log out
        """
        pass

    def __init__(self, username, password, email="None", fullName="None"):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__fullName = fullName
        Student.stusAccounts.update({f"{username}": f"{password}"})
        print(f"Welcome {self.__username}!\n")
