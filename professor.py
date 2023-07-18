class Professor:
    profs_accounts = {}  # {'username': password}

    @classmethod
    def get_profs_usernames(cls):
        return cls.profs_accounts.keys()

    @classmethod
    def get_prof_password(cls, username):
        return cls.profs_accounts.get(username)

    @classmethod
    def update_profs_accounts(cls, username, password):
        cls.profs_accounts.update({username: password})

    def __init__(self, username, password, full_name="None", email="None"):
        self.__username = username
        self.__password = password
        self.__full_name = full_name
        self.__email = email

    def create_course(self, course_name, TAs):
        pass

    def show_course_stats(self, hw_name):
        pass

    def create_hw(self, hw_name):
        pass

    def view_hw(self, hw_name):
        pass

    def grade_hw(self, hw_name):
        pass

    def show_hw_stats(self, hw_name):
        pass

    def prof_menu(self):
        temp = input("Welcome to the Professors menu!\n")

        option = input("Please make your choice:\n").strip()

        # Wrong Input
        while option not in []:
            option = input("Wrong input\n")

        # Back to main menu
        if option == "5":
            del self
        """
        List courses
        Create courses

        View Courses(List HW, Create HW, View HW(Show info, show grades report,
        list solutions, view solution (show info, set grade, set a comment, go back),
        Go back (== log out) ), Go back (== log out) )

        Log out (Returns to the sign in / sign up menu)
        """
