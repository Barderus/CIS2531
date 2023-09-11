'''
Author: Gabriel dos Reis
Date: 9 / 6 / 2023
Program: timeCalculator.py
Description: Write a program that asks the user to enter a number of second and work as follows:
    There are 60 seconds in a minute. 
    If the number of seconds entered by the user is greater than or equal to 60, 
    the program should convert the number of seconds to minutes and seconds.
                
    There are 3,600 seconds in an hour. 
    If the number of seconds entered by the user is greater than or equal to 3,600, 
    the program should convert the number of seconds to hours, minutes, and seconds.
                
              
    There are 86,400 seconds in a day. 
    If the number of seconds entered by the user is greater than or equal to 86,400, 
    the program should convert the number of seconds to days, hours, minutes, and seconds.
'''

userSeconds = int(input("Enter the number of seconds: "))

if userSeconds < 60:
    compMinutes = userSeconds % 60
    compSeconds = userSeconds // 60
    print(userSeconds, "seconds is equal to", compSeconds, "minutes and", compMinutes, "seconds.")
elif userSeconds < 86400:
    compHours = userSeconds // 3600
    compMinutes = userSeconds % 60
    compSeconds = userSeconds // 60

    print(userSeconds, "seconds is equal to", compHours, "hours,", compMinutes, "minutes and", compSeconds, "seconds.")
elif userSeconds >= 86400:
    compDays = userSeconds // 86400
    compHours = userSeconds // 3600
    compMinutes = userSeconds % 60
    compSeconds = userSeconds // 60
    print(userSeconds, "seconds is equal to", compDays, "days,", compHours, "hours,", compMinutes, "minutes and", compSeconds, "seconds.")
else:
    print("Sorry, I think there was a mistake. Try again.")

    
    