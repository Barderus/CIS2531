'''
'''
def main():
    # Open file for reading
    infile = open("students.txt", 'r')
    
    # Read names from file
    stu_name1 = infile.readline().rstrip("\n")
    stu_name2 = infile.readline().strip("\n")
    
    # Display student name
    print(stu_name1)
    print(stu_name2)
    
    # Close file
    infile.close()
    
main()   