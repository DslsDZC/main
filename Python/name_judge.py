#  Copyright (c) 2024.
#  There is no copyright leakage in this studio. If any infringement is found, legal responsibility will be investigated.

import getpass
import hashlib
import secrets

import Terminal_function


def generate_salt():
    return secrets.token_hex(16)


def hash_password(password ,salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()


def check_credentials(username ,password ,user_credentials):
    user_data = user_credentials.get(username)
    if user_data:
        return user_data["password"] == hash_password(password ,user_data["salt"])
    return False


def register_user(username ,password ,user_credentials):
    if username not in user_credentials:
        salt = generate_salt()
        hashed_password = hash_password(password ,salt)
        user_credentials[username] = {"salt":salt ,"password":hashed_password}
        print("User registered successfully!")
    else:
        print("Username already exists. Please choose a different username.")


def name_judge(user_credentials):
    try:
        name = input("Please enter your name: ").strip()
        key = getpass.getpass("Please enter the key of this studio: ").strip()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Program terminated.")
        return
    
    if not name or not key:
        print("Username or password cannot be empty.")
        return
    
    if check_credentials(name ,key ,user_credentials):
        print(f"Hello {name}!")
        print("Welcome to the DZC terminal.")
        Terminal_function.welcome_words()
    elif name not in user_credentials:
        if input("Username not found. Do you want to register? (yes/no): ").lower() == "yes":
            register_user(name ,key ,user_credentials)
        else:
            print("Registration cancelled.")
    else:
        print("Incorrect password input")


def init_user_credentials():
    credentials = {}
    for user ,pwd in [("DZC" ,"password123") ,("user2" ,"password456") ,("user3" ,"password789")]:
        salt = generate_salt()
        credentials[user] = {"salt":salt ,"password":hash_password(pwd ,salt)}
    return credentials


user_credentials = init_user_credentials()
name_judge(user_credentials)
