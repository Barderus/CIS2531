'''
Author: Gabriel dos Reis
Date: 9/12/2023
Program: bugCollector.py
Description: Prompt user for the amount of bugs collected each day for 5 days.
Display the total number of bugs collected.
'''

bug_collector = int(input("How many bugs did you collect today? "))
total_bugs = 0

for x in range (5):
    total_bugs =+ bug_collector + total_bugs

print(f"You captured {total_bugs} bugs in the past 5 days.")    
