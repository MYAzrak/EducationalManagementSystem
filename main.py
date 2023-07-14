# Modules imported
import sys
import Professor as Prof
import Student as Stu
import TeacherAssistant as TA
import re


# Functions defined
def enterDetails():
    """
    Used in the loginOption function.
    For users to input their usernames & passwords.
    """
    backToMainMenu = input("\nDo you want to go back to the main menu? (Y/N): ").strip()
    if backToMainMenu == "Y" or backToMainMenu == "y":
        main()
    else:
        username = input("Please enter your username: ").strip()
        password = input("Please enter your password: ").strip()
        return username, password


def isValidUsername(username):
    """
    Used in the registerAccount function.
    Validates usernames to have English letters, digits, a single dot, underscore, or dash characters only.
    """
    pattern = r"^(?!.*\..*\.)[a-zA-Z0-9_.-]{3,20}$"
    return re.match(pattern, username) is not None


def registerAccount(userRole):
    """
    Uses the isValidUsername function.
    Used in the registerOption function.
    Register accounts for all roles.
    """
    # Inputting username & password
    username = input("Please write your username: ").strip()
    while not isValidUsername(username):
        print("Incorrect username, please choose another one.")
        username = input(
            "Field should contain only English letters, digits, a single dot, underscore, or dash characters {3-20} in length.\n"
        ).strip()
    password = input("Please write your password: ").strip()

    # Professor registration
    if userRole == "P":
        if username in Prof.Professor.profsAccounts.keys():
            print("This username already exists. Going back to the login menu\n")
            main()
        else:
            Prof.Professor.profsAccounts.update({f"{username}": f"{password}"})
            print(f"Welcome {username}!\n")
            main()

    # Student registration
    elif userRole == "S":
        if username in Stu.Student.stusAccounts.keys():
            print("This username already exists. Going back to the login menu\n")
            main()
        else:
            Stu.Student.stusAccounts.update({f"{username}": f"{password}"})
            print(f"Welcome {username}!\n")
            main()

    # Teacher Assistant registration
    elif userRole == "T":
        if username in TA.TeacherAssistant.TAsAccounts.keys():
            print("This username already exists. Going back to the login menu\n")
            main()
        else:
            TA.TeacherAssistant.TAsAccounts.update({f"{username}": f"{password}"})
            print(f"Welcome {username}!\n")
            main()


def registerOption():
    option = input(
        "\nChoose your role to register:\n1. Professor\n2. Student\n3. Teacher Assistant\n4. Back\n"
    ).strip()

    # Wrong Input
    while option not in ["1", "2", "3", "4"]:
        option = input("Wrong input\n")

    # Professor registration
    if option == "1":
        registerAccount("P")

    # Student registration
    if option == "2":
        registerAccount("S")

    # Teacher Assistant registration
    if option == "3":
        registerAccount("T")

    # Back to main menu
    if option == "4":
        main()


def loginAccount(userRole, incorrectPasswordsLimit=3):
    """
    Uses the enterDetails function.
    Used in the loginOption function.
    Login accounts for all roles.
    """
    # 3 Invalid passwords attempts
    if incorrectPasswordsLimit == 0:
        sys.exit(1)

    # Input username & password without validation
    username, password = enterDetails()

    # Professor login
    if userRole == "P":
        if username not in Prof.Professor.profsAccounts.keys():  # Unavailable username
            print("This username does not exist.\n")
            loginAccount("P")
        else:
            if password == Prof.Professor.profsAccounts.get(
                username
            ):  # Correct password
                profUser = Prof.Professor(username, password)
                profUser.profMenu()
            else:  # Incorrect password
                print(
                    f"Incorrect password. {incorrectPasswordsLimit - 1} tries left.\n"
                )
                loginAccount("P", incorrectPasswordsLimit - 1)

    # Student login
    if userRole == "S":
        if username not in Stu.Student.stusAccounts.keys():  # Unavailable username
            print("This username does not exist.\n")
            loginAccount("S")
        else:
            if password == Stu.Student.stusAccounts.get(username):  # Correct password
                stuUser = Stu.Student(username, password)
                stuUser.stuMenu()
            else:  # Incorrect password
                print(
                    f"Incorrect password. {incorrectPasswordsLimit - 1} tries left.\n"
                )
                loginAccount("S", incorrectPasswordsLimit - 1)

    # Teacher Assistant login
    elif userRole == "T":
        if (
            username not in TA.TeacherAssistant.TAsAccounts.keys()
        ):  # Unavailable username
            print("This username does not exist.\n")
            loginAccount("T")
        else:
            if password == TA.TeacherAssistant.TAsAccounts.get(
                username
            ):  # Correct password
                TAUser = TA.TeacherAssistant(username, password)
                TAUser.TAMenu()
            else:  # Incorrect password
                print(
                    f"Incorrect password. {incorrectPasswordsLimit - 1} tries left.\n"
                )
                loginAccount("T", incorrectPasswordsLimit - 1)


def loginOption():
    option = input(
        "\nChoose your role to login:\n1. Professor\n2. Student\n3. Teacher Assistant\n4. Back\n"
    ).strip()

    # Wrong Input
    while option not in ["1", "2", "3", "4"]:
        option = input("Wrong input\n")

    # Professor option
    if option == "1":
        loginAccount("P")

    # Student option
    elif option == "2":
        loginAccount("S")

    # Teacher Assistant option
    elif option == "3":
        loginAccount("T")

    # Back to main menu
    elif option == "4":
        main()


# Main login menu
def main():
    # Register/Login options
    option = input(
        "\nWelcome to the EMS of your beloved university!\n1. Login\n2. Register\n3. Exit\n"
    ).strip()

    # Wrong Input
    while option not in ["1", "2", "3"]:
        option = input("Wrong input\n")

    # Login
    if option == "1":
        loginOption()

    # Register
    elif option == "2":
        registerOption()

    # Exit
    elif option == "3":
        sys.exit(0)


# Starting point
main()
