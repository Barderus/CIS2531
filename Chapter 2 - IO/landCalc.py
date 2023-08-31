'''
Author: Gabriel dos Reis
Date: 8/31/2023
Description: One acre of land is equivalent to 43,560 square feet. 
Write a program that asks the user to enter the total square feet in a tract of land 
and calculates the number of acres in the tract.
'''

ACRE_OF_LAND = 43560

userSqrFt = int(input("Enter total square feet in a land: "))
userAcre = userSqrFt / ACRE_OF_LAND
print(f"The total number of acres in the tract given is: {userAcre:.3f} acres of land." )

'''
Sample output:
Enter total square feet in a land: 10000
The total number of acres in the tract given is: 0.230 acres of land.
'''