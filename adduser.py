import os, subprocess

#Adds new user to the system
def new_user(): 
    confirm = "N" 
    while confirm != "Y":
        username = input("Enter the name of the user to add: ") 
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
        
    os.system("sudo adduser " + username)

new_user()