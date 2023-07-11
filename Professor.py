class Professor: 
    profsAccounts = {}

    def __init__(self, username, password, email = "None", fullName = "None"):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__fullName = fullName

    def createCourse(self, courseName, TAs):
        pass

    def showCourseStats(self, HWName):
        pass
    
    def createHW(self, HWName):
        pass

    def viewHW(self, HWName):
        pass

    def gradeHW(self, HWName):
        pass

    def showHWStats(self, HWName):
        pass

    def profMenu(self):
        '''
        List courses
        Create courses
        
        View Courses(List HW, Create HW, View HW(Show info, show grades report,
        list solutions, view solution (show info, set grade, set a comment, go back),
        Go back (== log out) ), Go back (== log out) ) 
        
        Log out (Returns to the sign in / sign up menu)
        '''
        pass