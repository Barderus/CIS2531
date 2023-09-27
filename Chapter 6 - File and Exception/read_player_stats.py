'''
Author: Gabriel dos Reis
Date: 9/27/2023
Program: read_payer.py
Description:
This program reads and display the following player statistics for the home
baseball team:
    Player first and last name --> character string
    Games played --> integer
    Home runs --> integer
Read the file for an indeterminate number of players and generate a team player report that includes
the above data for each player as well as a summary lines that includes the total number of players, the average number of games played
and the average number of home runs.
Player name should be displayed left aligned and the player statistics right aligned.
'''
# Named constant
FIELD_DELIMITIER = ":"
TICKER_WIDTH = 20
CMP_WIDTH = 10
YTD_WIDTH = 20
PRICE_WIDTH =20

def main():
    while True:
        try:
            # Get file name from user
            file_name = input("Enter file name: ")
            
            #Open the file for reading
            infile = open(file_name, 'r')
        except FileNotFoundError as err:
            print(err)

        else:
            print(str(format("Player Name", str(TICKER_WIDTH) + "s") + 
            format("Games Played", str(CMP_WIDTH) + "s") + 
            format("Home Runs", ">" + str(YTD_WIDTH) + "s")))
            # Counter for number of records
            num_players = 0
            #Accumulator to keep track of total games played
            total_games = 0
            #Accumulator to keep track of battling average
            total_battling = 0
            
            for line in infile:
                # Increment stock counter
                num_players += 1
                # Split out individual fields from line/record
                field_list  = line.split(FIELD_DELIMITIER)
                
                # parse each field as item in list
                name = field_list[0]
                games_played = int(field_list[1])
                home_runs = int(field_list[2])
                batting_average = float(field_list[3])
                
                # Accumulate the YTD percent
                total_games += games_played
                total_battling += batting_average
                
                # Display data in columnar format
            # Display data in columnar format using f-strings
            print(f"{name:<{TICKER_WIDTH}}{games_played:>{CMP_WIDTH}}{home_runs:>{YTD_WIDTH}}")
            print()
            
            # Display the summary statistics
            print("*** SUMMARY STATISTICS ***")          
            print(f"Total number of players read from file =  {num_players}")
            print(f"Average games played = {total_games/num_players:.3f}")  
            print(f"Overall batting average = {total_battling/num_players:.3f}")
            print()
            infile.close()
   
            break         
            

main()