class TeacherAssistant:
    tas_accounts = {}  # {'username': password}

    @classmethod
    def get_tas_usernames(cls):
        return cls.tas_accounts.keys()
    @classmethod
    def get_ta_password(cls, username):
        return cls.tas_accounts.get(username)
    @classmethod
    def update_tas_accounts(cls, username, password):
        cls.tas_accounts.update({username: password})

    def __init__(self, username, password, fullName="None", email="None"):
        self.__username = username
        self.__password = password
        self.__fullName = fullName
        self.__email = email

    def ta_menu(self):
        # Teacher Assistant menu
        temp = input("Welcome to the Teacher Assistants menu!\n")

        option = input("Please make your choice:\n1. Log out").strip()

        # Wrong Input
        while option not in ["1"]:
            option = input("Wrong input\n")

        # Back to main menu
        if option == "1":
            del self
