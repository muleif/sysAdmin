# This code imports the OS module the creates a fucntion to take user iput and adds to the System
# It uses adduser command to remove a user(input given) from the system

import os

def new_user(): 
    confirm = "N" 
    while confirm != "Y": 
        username = input("Enter the name of the user to add: ") 
        print("Use the username '" + username + "'? (Y/N)") 
        confirm = input().upper()
    os.system("sudo adduser " + username)

new_user()