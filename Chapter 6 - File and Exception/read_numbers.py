'''
'''
def main():
    #Open file for reading
    infile = open("stuCounts.txt", "r")
    
    # Read student count data
    count_today = int(infile.readline())
    count_yesterday = int(infile.readline())
    
    # Display the student counts and total
    print("Number of students in class today:", count_today)
    print("Number of students in class yesterday:", count_yesterday)
    print("Total students:", count_today + count_yesterday)
    
    # Close file
    infile.close()
    
main()