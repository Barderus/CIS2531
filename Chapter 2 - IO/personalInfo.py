'''
Author: Gabriel dos Reis
Date: 8/31/2023
Description: Write a program that displays the following information:
    *your name
    *Your address, with city, state, and ZIP         
    *your telephone number
    *Your college major
'''

userName = input("What is your full name?: ")
userAddress = input("Where do you live (street name): ")
userCity = input("What is the name of your city?: ")
userState = input("What is the state you are from?: ")
userZIP = input("What is the ZIP code?: ")
userPhoneNumber = input("What is your phone number?: ")
userMajor = input("What is your major?: ")

print("User information: ", "\n\tName: ", userName, \
    "\n\tAddress: ", userAddress, ",", userCity,",", userState,",", userZIP, \
        "\n\tPhone Number: ", userPhoneNumber, \
            "\n\tMajor: ", userMajor)

'''
Sample output:
User information:
        Name:  Gabriel dos Reis
        Address:  118 E 3rd St Hinsdale IL 60521
        Phone Number:  469-649-6982
        Major:  Computer Science
'''