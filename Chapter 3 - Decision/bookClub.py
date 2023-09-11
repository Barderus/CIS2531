'''
Author: Gabriel dos Reis
Date: 9/6/2023
Program: bookClub.py
Description: Write a program that asks the user to enter the number of books that he or she
has purchased this month, then displays the number of points awarded. 
    If 0 purchased, then they earn 0 points
    if 2 books were purchased, they earn 5 points
    If 4 books were purchased, they earn 15 points
    If 6 books were purchased, they earn 30 points
    If 8 books were purchased, they earn 60 points
'''

booksPurchased = int(input("How many books did you buy?: "))

if booksPurchased > 0 and booksPurchased < 2:
    print("Sorry, no points earned today.")
elif booksPurchased >= 2 and booksPurchased < 4:
    print("Congratulations! You earned 5 points!")
elif booksPurchased >= 4 and booksPurchased < 6:
    print("Congratulations! You earned 15 points!")
elif booksPurchased >= 6 and booksPurchased < 8:
    print("Congratulations! You earned 30 points!")
elif booksPurchased < 0:
    print("Sorry, I think there was a mistake. Try again.")
else:
    print("Congratulations! You earned 60 points!")