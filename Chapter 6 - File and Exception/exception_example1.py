'''
'''
def checkNegCount(count):
    if count < 0:
        raise ValueError("ERROR! Negative value entered!")
    
def main():
    # Prompt and read filename from user
    filename = input('Enter filename for recording of student counts: ')
    
    while True:
        try:
            # Open a file for output
            outfile = open(filename, 'w')
            #Get the student counts
            count_today = int(input('How many students are in class today? '))
            count_yesterday = int(input('How many students were in class yesterday? '))
            checkNegCount(count_today)
            checkNegCount(count_yesterday)
            
        except ValueError as err:
            print(err)
        except FileNotFoundError:
            print("ERROR! Could not find the file: " + filename)
        else:  
            # Write student counts to the file
            outfile.write(str(count_today) + '\n')
            outfile.write(str(count_yesterday) + '\n')
            # Close the file
            outfile.close()
            break
    print("Exciting the program...")
    
main()
    