class TeacherAssistant:
    TAsAccounts = {}

    @staticmethod
    def TAMenu():
        test = input("TA menu!")
        pass

    def __init__(self, username, password, email="None", fullName="None"):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__fullName = fullName
        TeacherAssistant.TAsAccounts.update({f"{username}": f"{password}"})
        print(f"Welcome {self.__username}!\n")

    
