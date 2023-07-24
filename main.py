# Modules imported
import re
from professor import Professor
from student import Student
from teacher_assistant import TeacherAssistant
from course import Course
from home_work import HomeWork


# Functions defined
def enter_details():
    """
    Used in the login_option function.
    For users to input their usernames & passwords.
    """
    back_to_main = input("\nDo you want to go back to the main menu? (Y/N): ").strip()
    if back_to_main == "Y" or back_to_main == "y":
        main()
    else:
        username = input("Please enter your username: ").strip()
        password = input("Please enter your password: ").strip()
        return username, password


def is_valid_username(username: str):
    """
    Used in the register_account function.
    Validates usernames to have English letters, digits, a single dot, underscore, or dash characters only.
    """
    pattern = r"^(?!.*\..*\.)[a-zA-Z0-9_.-]{3,20}$"
    return re.match(pattern, username) is not None


def register_account(user_role: str):
    """
    Uses the is_valid_username function.
    Used in the register_option function.
    Register accounts for all roles.
    """
    # Inputting username & password
    username = input("Please write your username: ").strip()
    while not is_valid_username(username):
        print("Incorrect username, please choose another one.")
        username = input(
            "Field should contain only English letters, digits, a single dot, underscore, or dash characters {3-20} in length.\n"
        ).strip()
    password = input("Please write your password: ").strip()

    # Professor registration
    if user_role == "P":
        # If username already exists
        if username in Professor.get_profs_usernames():
            print("This username already exists. Going back to the login menu\n")
            main()
        else:
            Professor.register_prof(username, password)
            print(f"Welcome {username}!\n")
            main()

    # Student registration
    elif user_role == "S":
        # If username already exists
        if username in Student.get_stus_usernames():
            print("This username already exists. Going back to the login menu\n")
            main()
        else:
            Student.register_stu(username, password)
            print(f"Welcome {username}!\n")
            main()

    # Teacher Assistant registration
    elif user_role == "T":
        # If username already exists
        if username in TeacherAssistant.get_tas_usernames():
            print("This username already exists. Going back to the login menu\n")
            main()
        else:
            TeacherAssistant.register_ta(username, password)
            print(f"Welcome {username}!\n")
            main()


def register_option():
    """
    Uses the register_account function
    """
    option = input(
        "\nChoose your role to register:\n1. Professor\n2. Student\n3. Teacher Assistant\n4. Back\n"
    ).strip()

    # Wrong Input
    while option not in ["1", "2", "3", "4"]:
        option = input("Wrong input\n")

    # Professor registration
    if option == "1":
        register_account("P")

    # Student registration
    if option == "2":
        register_account("S")

    # Teacher Assistant registration
    if option == "3":
        register_account("T")

    # Back to main menu
    if option == "4":
        main()


def login_account(user_role: str, incorrect_passwords_limit=3):
    """
    Uses the enter_details function.
    Used in the login_option function.
    Login accounts for all roles.
    """
    # 3 Invalid passwords attempts
    if incorrect_passwords_limit == 0:
        raise SystemExit("Are you a hacker?!")

    # Input username & password without validation
    username, password = enter_details()

    # Professor login
    if user_role == "P":
        if username not in Professor.get_profs_usernames():  # Unavailable username
            print("This username does not exist.\n")
            login_account("P")
        else:
            if password == Professor.get_prof_password(username):  # Correct password
                prof_user = Professor(username, password)
                prof_user.prof_menu()
                main()
            else:  # Incorrect password
                print(
                    f"Incorrect password. {incorrect_passwords_limit - 1} tries left.\n"
                )
                login_account("P", incorrect_passwords_limit - 1)

    # Student login
    if user_role == "S":
        if username not in Student.get_stus_usernames():  # Unavailable username
            print("This username does not exist.\n")
            login_account("S")
        else:
            if password == Student.get_stu_password(username):  # Correct password
                stu_user = Student(username, password)
                stu_user.stu_menu()
                main()
            else:  # Incorrect password
                print(
                    f"Incorrect password. {incorrect_passwords_limit - 1} tries left.\n"
                )
                login_account("S", incorrect_passwords_limit - 1)

    # Teacher Assistant login
    elif user_role == "T":
        if username not in TeacherAssistant.get_tas_usernames():  # Unavailable username
            print("This username does not exist.\n")
            login_account("T")
        else:
            if password == TeacherAssistant.get_ta_password(
                username
            ):  # Correct password
                ta_user = TeacherAssistant(username, password)
                ta_user.ta_menu()
                main()
            else:  # Incorrect password
                print(
                    f"Incorrect password. {incorrect_passwords_limit - 1} tries left.\n"
                )
                login_account("T", incorrect_passwords_limit - 1)


def login_option():
    """
    Uses the login_account function
    """
    option = input(
        "\nChoose your role to login:\n1. Professor\n2. Student\n3. Teacher Assistant\n4. Back\n"
    ).strip()

    # Wrong Input
    while option not in ["1", "2", "3", "4"]:
        option = input("Wrong input\n")

    # Professor option
    if option == "1":
        login_account("P")

    # Student option
    elif option == "2":
        login_account("S")

    # Teacher Assistant option
    elif option == "3":
        login_account("T")

    # Back to main menu
    elif option == "4":
        main()


def load_json():
    """
    Used in the starting point
    """
    Student.load_json_files()
    Professor.load_json_files()
    TeacherAssistant.load_json_files()
    Course.load_json_files()
    HomeWork.load_json_files()


def save_json():
    """
    Used in the starting point
    """
    Student.save_json_files()
    Professor.save_json_files()
    TeacherAssistant.save_json_files()
    Course.save_json_files()
    HomeWork.save_json_files()


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
        login_option()

    # Register
    elif option == "2":
        register_option()

    # Exit
    elif option == "3":
        pass


# Starting point
if __name__ == "__main__":
    # Load last session's data
    option = input("Do you want to load last session's data? (Y/N)\n").strip()
    if option == "Y" or option == "y":
        print("Loading...")
        load_json()

    main()

    # Save this session's data
    option = input("Do you want to save this session's data? (Y/N)\n").strip()
    if option == "Y" or option == "y":
        option = input(
            "NOTE: Last sessions' data will be lost! Are you sure? (Y/N)\n"
        ).strip()
        if option == "Y" or option == "y":
            print("Saving...")
            save_json()
