'''
Author: Gabriel dos Reis
Date: 9/6/2023
Program: WiFiDiagnostic.py
Description: Use the flowchart to create a program that leads a person through the steps
of fixing a bad Wi-Fi connection.'''

print("Reboot the computer and try to connect.")
fixTheProblem = input("Did that fix your problem?(YES/NO): ")

if fixTheProblem.lower() == "no":
    print("Reboot the router and try again.")
    fixTheProblem = input("Did that fix your problem?(YES/NO): ")
    if fixTheProblem.lower() == "no":
        print("Make sure the cables between the router & modem are plugged in firmly")
        fixTheProblem = input("Did that fix your problem?(YES/NO): ")
        if fixTheProblem.lower() == "no":
            print("Move the router to a new location and try to connect.")
            fixTheProblem = input("Did that fix the problem? (YES/NO): ")
            if fixTheProblem.lower() == "no":
                print("get a new router")
            else:
                print("Problem solved. Thank you for calling us.")
        else:
            print("Problem solved. Thank you for calling us.")
    else:
        print("Problem solved. Thank you for calling us.")
else:
    print("Problem solved. Thank you for calling us.")
    