import os
import subprocess


# install or remove packages

def install_or_remove_packages():
    iOrR = "" 
    while iOrR != "I" and iOrR != "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR = input().upper()
        
    if iOrR == "I": 
        iOrR = "install"
        
    elif iOrR == "R": 
        iOrR = "remove"
        
    print("Enter a list of packages to install") 
    print("The list should be separated by spaces, for example:") 
    print(" package1 package2 package3") 
    print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program") 
    packages = input().lower() 
    
    if packages == "default": 
        packages = ""
        os.system("sudo yum update -y")
        os.system("sudo yum upgrade -y")
        
    if iOrR == "install":
        os.system("sudo yum install " + packages + " -y")
        
    elif iOrR == "remove": 
        while True: 
            print("Purge files after removing? (Y/N)") 
            choice = input().upper() 
            
            if choice == "Y":
                os.system("sudo yum " + iOrR + " " + packages + " -y") 
                os.system("sudo yum autoremove -y") 
                break
            
            elif choice == "N":
                os.system("sudo yum " + iOrR + " " + packages + " -y") 
                break

        
#Cleans the environment after an uninstall    
def clean_environment(): 
        os.system("sudo yum autoremove") 
        # os.system("sudo yum autoclean")
        
#Updates the default modules
def update_environment():
    os.system("sudo yum update") 
    os.system("sudo yum upgrade") 
    os.system("sudo yum update --security")