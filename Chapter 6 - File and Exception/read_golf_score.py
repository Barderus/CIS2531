'''
Read the contents of golf.txt
'''
FIELD_DELIMITIER = ":"

def main():
        
        # Keep looking until the correct input is entered
    while True:
        try:
            # Get a file name from user
            filename = input("Enter filename for reading: ")
            
            # Open file for reading
            infile = open(filename, "r")
        # Exception to handle file not found
        except FileNotFoundError as err:
                print(err)
        # Generic exception to handle any file error
        except IOError as err:
                print(err)
        # To catch any other error
        except ValueError as err:
            print(err)
        else:
            # Loop to read each line of the file and print each record               
            for line in infile:
                field_list  = line.split(FIELD_DELIMITIER)
                    
                # parse each field as item in list
                name = field_list[0]
                golf_score = int(field_list[1])        
        # Display the values
        print(f"{'Name:':<20}{'Golf score:':>15}")
        print(f"{name:<15}{golf_score:>15}")
        infile.close()
        break

# Call the main function       
main()