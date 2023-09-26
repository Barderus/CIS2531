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
    
    # Prompt user for the file name
    filename = input("Enter the file name: ")
    
    # Open the file for output
    outfile = open(filename, "w")
    
    while True:
        try:
            # Prompt user for how many players to record
            player_rec = int(input("How many player statistics would you like to record?: "))
            print()
            
            for r in range(player_rec):
                player_name = input("Enter player name: ")
                games_played = int(input("Enter the number of games played: "))
                home_runs = int(input("Enter the number of home runs: "))
                battling_avg = float(input("Enter the battling average: "))
                
                # Create a delineated record of player data
                player_str = player_name + FIELD_DELIMITER + str(games_played) + FIELD_DELIMITER + str(home_runs) + FIELD_DELIMITER + str(battling_avg)
            
                # Write record out to file
                outfile.write(player_str + "\n")      
        except ValueError:
            print("ERROR!")           
        else:
            # Close the file
            outfile.close()
            print("Records written to", filename + ".")
            break            
        finally:
            print("Exiting the program.")

# Call the main function
if __name__ == '__main__':
    main()