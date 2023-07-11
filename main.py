# Modules imported
import sys
import Professor

# Functions defined


def enterDetails():
    username = input("Please enter your username: ").strip()
    password = input("Please enter your password: ").strip()
    return username, password


# Data initialized
options = ["1", "2", "3", "4"]


# Login menu
while True:
    # Input option
    option = input(
        "Welcome to the EMS of your beloved university!\nPlease choose your role:\n1. Professor\n2. Student\n3. Teacher Assistant\n4. To exit\n"
    ).strip()
    
    # Wrong Input
    while option not in options:
        option = input("Wrong input\n")
    
    # Exit
    if option == "4":
        sys.exit(0)
    
    # Input username & password without validation
    username, password = enterDetails()
    
    # Professor option
    if option == '1':
        while username not in Professor.profsAccounts:
            pass

    # Student option
    elif option == '2':
        pass

    # Teacher Assistant option
    else:  
        pass














# Use it if you want to add (Create an account) function
# def validateUsername(username):
#     pattern = r"^(?!.*\..*\.)[a-zA-Z0-9_.-]{3,20}$"
#     return re.match(pattern, username) is not None

# while(not validateUsername(username)):
#     username = input("Incorrect username. Field should contain only English letters, digits, a single dot, underscore, or dash characters").strip()
