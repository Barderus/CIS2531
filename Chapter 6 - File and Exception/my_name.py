'''
Write a program that opens an output file with the filename my_name.txt, writes your name to the file,
then closes the file.
'''

def main():
    
    # File name
    filename = "my_name.txt"
    
    #Open file
    outfile  = open(filename, "w")
    
    # Write on the file
    user_name = input("Enter your name: ")
    outfile.write(user_name)
    
    print("Input was written on", filename)
    
    #Close file
    outfile.close()
    
main()
    
    