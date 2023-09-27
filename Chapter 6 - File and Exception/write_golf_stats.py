'''
Golf scores
Write a program that read each player's name and golf score as input, then save these records
in a file named golf.txt.
Then create another file to read the records of golf.txt file and displays them.

'''
# Named constant
FIELD_DELIMITER = ":"

def main():
    
    # Filename
    filename = "golf.txt"
    
    while True:
        try:
            while True:
                # Making sure the records are valid non-negative integers
                try:
                    number_records = int(input("How many records would you like to create?: "))
                    if number_records > 0:
                        break
                    else:
                        print("ERROR! You have to enter at least one record entry.")
                except ValueError as err:
                    print("ERROR! Please enter a valid integer for the number of record entries.")
                
            # Open the file in append mode
            outfile = open(filename, "w")
            
            # Loop to go through each 
            for r in range(number_records):
                player_name = input("Enter the player name: ")
                while True:
                    try:
                        golf_score = int(input("Enter the golf score: "))
                        if golf_score >= 0:
                            break
                        else:
                            print("ERROR! The score cannot be negative.")
                    except ValueError:
                        print("ERROR! Please enter a valid integer for golf score.")
                
                # Create a delimiter-separated record entry
                record_entry = player_name + FIELD_DELIMITER + str(golf_score)
                
                # Write the record to the file
                outfile.write(record_entry + "\n")
                
                # Print confirmation
                print("Record written to", filename)
            
            # Close the file
            outfile.close()
            
            # If all records were processed successfully, print a message
            print("All records have been successfully written to", filename)
            break
        except IOError as err:
            print(err)
        except ValueError as err:
            print(err)
        finally:
            print("Exiting program...")

main()

            