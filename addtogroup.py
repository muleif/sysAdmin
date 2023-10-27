import subprocess
import os
#Adds user to group

def user_exists(username):
    try:
        subprocess.check_call(["id", username])
        return True
    except subprocess.CalledProcessError:
        return False
    
def add_user_to_group():
    username = input("Enter the name of the user that you want to add to a group: ") 
    if not user_exists(username):
        print(f"User '{username}' does not exist.")
        return
    output = subprocess.Popen('groups', stdout=subprocess.PIPE, text=True).communicate()[0] 
    print("Enter a list of groups to add the user to") 
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3") 
    print("The available groups are: ")
    print(output) 
    chosenGroups = input("Groups: ")
    output = output.split(" ") 
    print("Add To: " + chosenGroups) 
    chosenGroups = chosenGroups.split(" ") 
    groupString = ""
    
    for grp in chosenGroups:
        if grp in output:
            print(f"Group {grp} found")
            groupString = groupString + grp + ","

        else:
            print(f"Group {grp} not found. Please first add group to the system")
            
    groupString = groupString[:-1] + " " 
    confirm = ""
    
    while confirm != "Y" and confirm != "N" : 
        print("Add user '" + username + "' to these groups? " + groupString + " (Y/N)") 
        confirm = input().upper()
        
    if confirm == "N": 
        print("User " + username + " not added")
    elif confirm == "Y":
        os.system("sudo usermod -aG " + groupString + username) 
        print("User "+ username + " added")
        


add_user_to_group()
        

