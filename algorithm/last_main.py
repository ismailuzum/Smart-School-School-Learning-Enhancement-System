from last_system import *

if __name__ == "__main__":
    filename = "user_data.json"
    system = SchoolManagementSystem()
    system.get_users(filename)

    while True:
        selection = input('''
For Login, press 1
For Register, press 2
For Quit, press q                          
Selection: ''')
        
        if selection == "1":
            user = system.loginRequest(email=input("Please enter your email: "), password=input("Please enter your password: "))
            if user:
                if user.user_status == "admin":
                    selection = input('''
For add a Teacher, select 1
For edit a Teacher, select 2
For Logout, select q
Selection: ''')
                    if selection == "1":
                        first_name = input("Enter your first name: ")
                        last_name = input("Enter your last name: ")
                        email = input("Enter your email: ")
                        password = input("Enter your password: ")
                        if system.isEmailUnique(email):
                            if system.emailValidator(email):
                                if system.passwordValidator(password):
                                    system.registerRequest(first_name, last_name, email, password, "teacher")
                                    print("Registration successfull")
                                else:
                                    print("Wrong Password Format")
                            else:
                                print("Wrong Email Format")
                        else:
                            print("There is an account matched with this email")
                    
                    elif selection == "2":
                        email = input("Enter teacher email: ")
                        first_name = input("Enter teacher new first name: ")
                        last_name = input("Enter teacher new last name: ")
                        password = input("Enter teacher new password: ")
                        system.editRequest(email, user, first_name=first_name, last_name=last_name, password=password)
                    elif selection == "3":
                        print("LOGOUT")
                        user = None

        elif selection == "2":
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if system.isEmailUnique(email):
                if system.emailValidator(email):
                    if system.passwordValidator(password):
                        system.registerRequest(first_name, last_name, email, password, "student")
                        print("Registration successfull")
                    else:
                        print("Wrong Password Format")
                else:
                    print("Wrong Email Format")
            else:
                print("There is an account matched with this email")
                
            
        elif selection == "q":
            system.post_users(filename)
            print("Goodbye")
            exit()
