"""
################################################################################################################
Description : This script take pdf file and password as input and remove password from pdf file
              and store outfile in same path
################################################################################################################
"""
import pikepdf
import time
print("#########################################################################")
print("##                                                                     ##")
print("##                 Welcome to PDF Password Remover Tool                ##")
print("##                       Develop by Sumit Wankhede                     ##")
print("##                                                                     ##")
print("#########################################################################")
i = True
while i:
    path = input("Enter file path : ")
    password = input("Enter Password : ")
    try:
        try:
            removePass = pikepdf.open(path, password=password)  # pikepdf function open file with pass
            path = path.split('.')[0]
            removePass.save(path + "_pass_remove.pdf")  # saving output file
            print("Output file : " + path + "_pass_remove.pdf")  # printing output path
            print("Process Finished")
            i = False
        except pikepdf.PasswordError:
            print("Error: Incorrect password ! Try Again")  # Exception handling for Incorrect password
    except IOError:
        print("Error: can\'t find file or read data ! Try Again")  # Exception handling for Incorrect path
time.sleep(10)
