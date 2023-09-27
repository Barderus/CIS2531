'''
Write a program that opens the my_name.txt file. Reads your name from the file, displays the name
on the screen, then closes the file.
'''

def main():
    
    # Filename
    filename = "my_name.txt"
    
    #Open file
    infile = open(filename, "r")
    
    # Read the file
    name = infile.readline()
    
    # Print name
    print(name)
    
    # Close the file
    infile.close()
    
main()
    