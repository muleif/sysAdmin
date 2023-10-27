
import os
#Removes user from system        
def remove_user():
    confirm = "N" 
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ")
        print("Remove the user : '" + username + "'? (Y/N)")
        confirm = input().upper()
    
    os.system("sudo userdel -r " + username)