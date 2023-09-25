'''
'''
def main():
    # Get name from user
    stu_name1 = input("Enter student name: ")
    stu_name2 = input("Enter student name: ")
    
    # Open file for output
    outfile = open("students.txt", "w")
    
    # Write out names to file
    outfile.write(stu_name1 + "\n")
    outfile.write(stu_name2)
    
    # Close file
    outfile.close()
    
main()