'''
Author: Gabriel dos Reis
Date: 9/5/2023
Program: testAvg.py
Description: This program gets three input scores and displays
their average. The user is congratulated if the average score
is higher than 95.
'''

#Named constants for high scores
HIGH_SCORE = 95

# Get the three input test scores
test1 = int(input("Enter the score for test 1:"))
test2 = int(input("Enter the score for test 2:"))
test3 = int(input("Enter the score for test 3:"))

# Calculate the average
average = (test1 + test2 + test3) / 3

#Display the average score
print(f"The average score is {average:.1f}")

# Check if it is high score
if average >= HIGH_SCORE:
    print("Congratulations!")
    print("That is a great average and a high score!")

'''
Sample output:
Enter the score for test 1:100
Enter the score for test 2:99
Enter the score for test 3:87
The average score is 95.3
Congratulations!
That is a great average and a high score!
'''