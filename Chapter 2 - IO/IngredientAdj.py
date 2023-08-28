'''
Author: Gabriel dos Reis
Date: 8/28/2023
Class: CIS 2531 - Intro to Python
Prog: ingredientAdj.py
Description: A cookie recipe produces 48 cookies with following ingredients:
1.5 cups of sugar
1 cup of butter
2.75 cups of flour
Prompt user for how many cookiesthey want to make and display the amount of each ingredient
is necessary to make the specified number of cookies
'''

#named constants for the ingredients ratio
CUPS_OF_SUGAR = 1.5
CUPS_OF_BUTTER = 1
CUPS_OF_FLOUR = 2.75
COOKIES = 48

#Prompt user for quantity of cookies
userCookies = int(input("Enter the amount of cookies you would like to make: "))

# Calculations
ttlSugar = (CUPS_OF_SUGAR * userCookies) / COOKIES
ttlButter = (CUPS_OF_BUTTER * userCookies) / COOKIES
ttlFlour = (CUPS_OF_FLOUR * userCookies) / COOKIES

# Print the output
print(f"You will need:\n\t{ttlSugar:.3f} cups of sugar \
        \n\t{ttlButter:.3f} cups of butter \
            \n\t{ttlFlour:.3f} cups of flour")
