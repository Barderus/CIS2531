'''
'''

def main():
    # Open a file for output
    outfile = open('stuCounts.txt', 'w')
    
    #Get the student counts
    count_today = int(input('How many students are in class today? '))
    count_yesterday = int(input('How many students were in class yesterday? '))
    
    # Write student counts to the file
    outfile.write(str(count_today) + '\n')
    outfile.write(str(count_yesterday) + '\n')
    
    # Close the file
    outfile.close()
    
main()
    