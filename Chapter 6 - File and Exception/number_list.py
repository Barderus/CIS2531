'''
Write a code that opens an output file with the filename number_list.txt, uses a loop to
write the numbers 1 through 100 to the file, then closes the file
'''

def main():
    
    # Filename
    filename = "number_list.txt"
    
    # Open file
    outfile = open(filename, "w")
    
    # Write number 1 through 100
    for x in range(1,101):
        outfile.write(str(x) + "\n")
        x +=1
        
    # Close the file
    outfile.close()
    
main()