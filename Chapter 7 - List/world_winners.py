'''
World Series Champions
If you have downloaded the source code you will find a file named WorldSeriesWinners. txt in the Chapter 07 folder. 
This file contains a chronological list of the World Series winning teams from 1903 through 2009. 
(The first line in the file is the name of the team that won in 1903, and the last line is the name of the team that won in 2009. 
Note the World Series was not played in 1904 or 1994.)
Write a program that lets the user enter the name of a team, 
then displays the number of times that team has won the World Series in the time period from 1903 through 2009.
'''

def main():
    
    # File with information from the World Series Winner
    filename = "WorldSeriesWinners.txt"
    
    # Open file
    infile = open(filename, "r")
    
    # Read the data and strips new line, store the document data into the winner_list
    read_data = infile.read()
    winner_list = read_data.split("\n")
    # print(winner_list)
    
    # Close file
    infile.close()
    
    # Prompt user for the baseball team
    check_winner = input("What baseball team are you looking to check?(1903 - 2009): ")
    
    # Display how many times the team won
    print(f"{check_winner} has won {winner_list.count(check_winner)} times.") 
    
# Call main   
if __name__ == "__main__":
    main()