#this code add the use of subprocess to get a list of groups and pipe the standard output to a variable output


import os
import subprocess

def add_user_to_group(): 
    username = input("Enter the name of the user that you want to add to a group: ") 
    output = subprocess.Popen('groups', stdout=subprocess.PIPE, text=True).communicate()[0] 
    print("Enter a list of groups to add the user to") 
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3") 
    print("The available groups are:\r\n " + output) 
    chosenGroups = str(input("Groups: "))

    output = output.split(" ") 
    
    print("Add To:" + chosenGroups) 
    chosenGroups = chosenGroups.split(" ") 
    groupString = ""

    for grp in chosenGroups:
        if grp in output:
            print(f" Group {grp} found")
            groupString = groupString + grp + ","
            confirm = ""
            while confirm != "Y" and confirm != "N" : 
                print("Add user '" + username + "' to these groups? (Y/N)") 
                confirm = input().upper()
                if confirm == "Y": 
                    os.system("sudo usermod -aG " + groupString + username) 
                    
                    print("User '" + username + "'  added")
                elif confirm == "N": 
                    print("User " + username + " not added")
        else:
            print(f"Group {grp} not found. Add the group to the system first") 
       


add_user_to_group()