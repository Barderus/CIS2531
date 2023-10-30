'''
Author: Gabriel dos Reis
Date: 10/16/2023
Program: unpickleSets.py
Description: Example of unserializing (unpickling) sets of class name from file
'''

import pickle

def main():
    
    # get filename from user
    filename = input("Enter the file to store students in classes: ")
    
    # Open a file for binary reading
    infile = open(filename, "rb")
    
    eof = False # To indicat end of file
    
    # Read to the end of the file
    while not eof:
        try:
            # Unpickle the next object
            classNames = pickle.load(infile)
            
            # Display the object
            print("Class names: ")
            for students in classNames:
                print(f"\t{students}")
        except EOFError:
            # Set the flag to indicate the end
            eof = True
    
    # Close the file
    infile.close()
    

# Call the main function
if __name__ == "__main__":
    main()