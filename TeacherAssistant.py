class TeacherAssistant:
    TAsAccounts = {}

    @staticmethod
    def TAMenu():
        test = input("TA menu!")
        pass

    def __init__(self, username, password, fullName, email="None"):
        self.__username = username
        self.__password = password
        self.__fullName = fullName
        self.__email = email
        TeacherAssistant.TAsAccounts.update({f"{username}": f"{password}"})
        print(f"Welcome {self.__username}!\n")

