
# This code imports the OS module the creates a fucntion to take user iput and deletes to the System
# It uses userdel function to remove a user(input given) from the system

import os

def remove_user(): 
    confirm = "N" 
    while confirm != "Y": 
        username = input("Enter the name of the user to remove: ") 
        print("Use the username '" + username + "'? (Y/N)") 
        confirm = input().upper()
    os.system("sudo userdel -r " + username)

remove_user()