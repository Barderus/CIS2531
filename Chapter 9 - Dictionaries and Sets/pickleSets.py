'''
Serializing Objects
'''
'''
Author: Gabriel dos Reis
Date: 10/16/2023
Program: pickleSets.py
Description: Example of serializing (pickling) sets of class name to file
'''

# Import pickle module
import pickle

def saveClassNames(outfile):
    
    # Create an empty set
    classNames = set()
    
    # Get student names for set
    name = input("Enter student name (DONE to quit): ")
    
    # Loop while names to add to set
    while name!= "DONE":
        #Add name to set
        classNames.add(name)
        
        #See if another name
        name = input("Enter another student name (DONE to quit): ")
    
    # Pickle the set to file
    pickle.dump(classNames, outfile)

def main():
    
    # get filename from user
    filename = input("Enter the file to store students in classes: ")
    
    # Open a file for binary writing
    outfile = open(filename, "wb")
    
    # Loop while class data t write
    again = "y"
    while again.lower() == "y":
        # Save set of students names to file
        saveClassNames(outfile)
        
        # See if user wants to enter more data
        again = input("Enter more class students? (y/n): ")
    
    outfile.close()

# Start program by calling main
if __name__ == "__main__":
    main()