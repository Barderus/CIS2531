'''
Author:
Date:
Prorgram:
Description:
'''

KILOMETER_TO_MILES = 0.6214

def showMiles(*kilometers):
    ''' This is a function to calculate and display MPH given KPH.
    
    Parameters:
        Kilometers (float): kilometer per hour
        
    Process:
        Convert kilometers to miles using the following formula:
            miles = kilometers * 0.6214
        Display kilometers and converted miles.
        '''
        
    # local variable to hold miles
    miles = 0.0
    # Loop over each value passed
    for kilo in kilometers:
        miles = kilo * KILOMETER_TO_MILES
        print("The conversion of", format(kilo,".2f"), "kilometers to miles is", format(miles, ".2f"), "miles.")
        print()

#print(showMiles.__doc__)
showMiles(60, 70, 80, 90, 100)