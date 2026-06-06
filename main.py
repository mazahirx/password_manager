import random
import string
import os

passwords = {}

def generate_password():
    characters = (
        string.ascii_letters + 
        string.digits + 
        string.punctuation
    )
    print(f"Password Generated : {password}")                   

def add_password():
    pass_name = input("Enter the name to store the password with : ")
    pass_code = input("Enter your password : ")

    passwords[pass_name] = pass_code
    print("Password Stored")

def view_password():
    if len(passwords) == 0:
        print("No passwords stored")
    
    for pass_name in passwords:
        print(f"Name : {pass_name} \nPassword : {passwords[pass_name]}")

def save_password():

    full_path = os.path.join("password_manager","passwords.txt")
    file = open(full_path, "w")

    for pass_name in passwords:
        file.write(f"{pass_name} : {passwords[pass_name]}")

    file.close()

def main():

    while True:
        print("------   PASSWORD MANAGER   ------")
        print("\n1. Generate Password")
        print("2. Add Password")
        print("3. View Passwords")
        print("4. Save Passwords")
        print("5. Exit")

        choice = int(input("Choice an option : "))

        if choice == 1:
            generate_password()

        elif choice == 2:
            add_password()

        elif choice == 3:
            view_password()

        elif choice == 4:
            save_password()

        elif choice == 5:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()