'''
Create a program to save the following player statistics for the
home baseball team:
    Number of players --> Integer
    Player First and Last Name --> character String
    Games Played --> integer
    Home runs --> integer
    Batting Average --> floating point
Prompt and read the above data and write it out to a sequential ASCII text file.
    Include:
        Allow user entry of the file name
        Descriptive prompts
        Exception handling(only positice numerical values)
            Error to handle:
                Negative or non-integer number of players
                Invalid filename
                Negative or non-integer number of games played
                Negative or non-integer number of home runs
                Negative or non-float number of batting average
        
'''
# Named constant
FIELD_DELIMITER = ":"

def main():
    try:
        # Prompt user for the file name
        filename = input("Enter the file name: ")
        
        # Prompt user for how many players statistic to record
        # Try/Except checks for non-integer numbers or characters.
        while True:
            try: 
                player_rec = int(input("How many player statistics would you like to record?: "))
            
                if player_rec >= 0:
                    break  # Exit the loop if a valid positive integer is entered
                else:
                    print("ERROR! Number of players cannot be negative.")
            except ValueError:
                print("ERROR! Please enter a valid integer for the number of players.")
        
        # Open the file for output using a 'with' statement
        with open(filename, "w") as outfile:
            for r in range(player_rec):
                player_name = input("Enter player name: ")
                
                # Prompt for number of games played until a valid positive integer is entered
                while True:
                    try:
                        games_played = int(input("Enter the number of games played: "))
                        if games_played >= 0:
                            break
                        else:
                            print("ERROR! Games played cannot be negative.")
                    except ValueError:
                        print("ERROR! Please enter a valid integer for games played.")
                
                # Prompt for number of home runs until a valid positive integer is entered
                while True:
                    try:
                        home_runs = int(input("Enter the number of home runs: "))
                        if home_runs >= 0:
                            break
                        else:
                            print("ERROR! Home runs cannot be negative.")
                    except ValueError:
                        print("ERROR! Please enter a valid integer for home runs.")
                
                # Prompt for battling average until a valid positive float or integer is entered
                while True:
                    try:
                        battling_avg = float(input("Enter the batting average: "))
                        if battling_avg >= 0:
                            break
                        else:
                            print("ERROR! Batting average cannot be negative.")
                    except ValueError:
                        print("ERROR! Please enter a valid float for batting average.")
                
                # Create a delimited record of player data
                player_str = player_name + FIELD_DELIMITER + str(games_played) + FIELD_DELIMITER + str(home_runs) + FIELD_DELIMITER + str(battling_avg)
            
                # Write the record out to the file
                outfile.write(player_str + "\n")
        
        print("Records written to", filename)
    except IOError:
        print("Error: Invalid filename or unable to write to the file.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("Exiting program...")

# Call main
if __name__ == '__main__':
    main()
