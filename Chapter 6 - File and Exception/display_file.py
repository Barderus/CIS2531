'''
This program displays the contents of a file
'''

def main():
    while True:
        try:
            # Get the name of a file
            filename = input("Enter a filename: ")
            
            # Open the file
            infile = open(filename, 'r')
            
            # Read the file's contents
            contents = infile.read()
        except FileNotFoundError:
            print("ERROR! It cannot find the file", filename)
        except IOError:
            print("ERROR! An error occurred trying to read the file", filename)
        else:
            # Display the file's contents
            print(contents)
            # Close the file
            infile.close()
            break
    
# Call the main function
if __name__ == '__main__':
    main()