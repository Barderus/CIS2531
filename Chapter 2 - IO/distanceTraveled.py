'''
Author: Gabriel dos Reis
Date: 8/31/2023
Description: Assuming there are no accidents or delays, the distance that a car travels 
down the interstate can be calculated with the following formula:  
                Distance = Speed x Time
A car is traveling at 70 miles per hour. Write a program that displays the following:
                
    The distance the car will travel in 6 hours
    The distance the car will travel in 10 hours
    The distance the car will travel in 15 hours
'''

CAR_SPEED = 70

firstTravel = CAR_SPEED * 6
secondTravel = CAR_SPEED * 10
thirdTravel = CAR_SPEED * 15

print("In 6 hours that will have traveled: ", firstTravel, "miles")
print("In 10 hours that will have traveled: ", secondTravel, "miles")
print("In 15 hours that will have traveled: ", thirdTravel, "miles")