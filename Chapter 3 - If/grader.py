'''
Author: Gabriel dos Reis
Date: 9/5/2023
Program: grader.py
Description: Based on numeric score, calculate grade
'''

# Get score from user
score = int(input("Enter your test score: "))

# Determine the grade
if score >= 90:
    print("Your grade is A! Execellent")
elif score >= 80:
    print("Your grade is B!")
elif score >= 70:
    print("Your gradde is C!")
elif score >= 60:
    print("Your grade is D!")
else:
    print("Your grade is F.")
    
'''
# Determine the grade
if score >= 90:
    print("Your grade is A! Execellent")
else:
    if score >= 80:
        print("Your grade is B!")
    else:
        if score >= 70:
            print("Your gradde is C!")
        else:
            if score >= 60:
                print("Your grade is D!")
            else:
                print("Your grade is F.")
'''