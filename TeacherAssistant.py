from main import main


class TeacherAssistant:
    TAsAccounts = {}

    def __init__(self, username, password, fullName="None", email="None"):
        self.__username = username
        self.__password = password
        self.__fullName = fullName
        self.__email = email

    def TAMenu(self):
        # Teacher Assistant menu
        temp = input("Welcome to the Teacher Assistants menu!\n")
        
        option = input("Please make your choice:\n1. Log out").strip()

        # Wrong Input
        while option not in ["1"]:
            option = input("Wrong input\n")

        # Back to main menu
        if option == "1":
            del self
            main()
