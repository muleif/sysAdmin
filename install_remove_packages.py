# use this code for ubuntu based systems
# fro centos like restart labs, replace apt with yum. The rest of the code remains the same


import os

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
        os.system("sudo apt update -y")
    if iOrR == "install": 
        os.system("sudo apt install " + packages + " -y")

    elif iOrR == "remove": 
        while True: 
            print("Purge files after removing? (Y/N)") 
            choice = input().upper() 
            if choice == "Y": 
                os.system("sudo apt --purge " + iOrR + " " + packages + " -y") 
                break
            elif choice == "N": 
                os.system("sudo yum " + iOrR + " " + packages + " -y") 
                break




install_or_remove_packages()