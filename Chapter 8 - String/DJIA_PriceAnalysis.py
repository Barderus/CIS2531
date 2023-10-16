'''
Author: Gabriel dos Reis
Date: 10/10/2023
Program: DJIA_PriceAnalysis.py
Purpose: Implement a Python program to use a data file containing the daily closing price
for the DJIA for any given number of months and years and sortin date ordedr,
to produce a yearly DJIA analysis report that displays the aveage DJIA for each month in each year
of data contained within the file.

    * Each line in the data file contains the closing price for a date
            MM/DD/YYYY, Price
                MM -> One or two digit month
                DD -> One or two digit day
                YYYY -> Four digit year
    *The field separator is a comma
    
Requirements:
    * Modular Approach
    * Function to read file into list and return list
    * Processing list parameters to create formatted output report display
    * Prompt and read filename containing the data to read
'''
# Constant variable
FIELD_DELIMITER = ","

# Function that reads the file and append the data into two lists, one with the dates and one with the price
def readFile(filename, ):
    
    # Initialize lists
    dateList = []
    priceList = []
    
    infile = open(filename, "r")
    
    # Loop to taht reads the file and append the data into the respective list
    for line in infile:
        field_list  = line.strip().split(FIELD_DELIMITER)
        date, price = field_list
        dateList.append(date)
        priceList.append(float(price))
    infile.close()
    
    return dateList, priceList 
 
# Function that displays the analysis report and calculates the average price of each month
def displayOutput(dateList, priceList):
    
    message = "DJIA closing price averages for "
    monthMsg = "MONTH"
    avgMsg = " AVERAGE"
    delimiterMsg = "="
    monthList = ["January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]
    
    # Initialize variables to track the current month and accumulate prices
    current_month = None
    monthly_total = 0
    monthly_count = 0
    currentYear = None  

    '''
    ZIP (https://docs.python.org/3/library/functions.html#zip)
    zip() returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument iterables.
    Another way to think of zip() is that it turns rows into columns, and columns into rows. This is similar to transposing a matrix.
    '''
    for date, price in zip(dateList, priceList): # Use of zip to iterate through elements of two lists simultaneously
        # Separates the data into three variables
        month, day, year = date.split("/")
        day = int(day)
        month = int(month)      
        year = int(year)
        
        # Check if the year has changed so it can display th proper header
        if year != currentYear:
            if currentYear is not None:
                # Calculate and display the average for the previous month
                monthly_average = monthly_total / monthly_count
                monthly_name = monthList[current_month - 1]
                print(f"{monthly_name:>20}\t{monthly_average:>20,.2f}")

            # Reset variables for the new year
            currentYear = year
            current_month = month
            monthly_total = price
            monthly_count = 1

            # Display DJIA closing price averages for YYYY
            print(f"\n{message} {year}")

            # Display the table headers
            #               Month           Average
            #               =====           =======
            print(f"{monthMsg:>20}\t{avgMsg:>20}")
            print(f"{(delimiterMsg*5):>20}\t{(delimiterMsg*7):>20}")
        else:
            # Check if the month has changed so it will calculate the average to the right month
            if month != current_month:
                # Calculate and display the average for the previous month
                monthly_average = monthly_total / monthly_count
                monthly_name = monthList[current_month - 1]
                print(f"{monthly_name:>20}\t{monthly_average:>20,.2f}")

                # Reset variables for the new month
                current_month = month
                monthly_total = price
                monthly_count = 1
            else:
                # Accumulate prices for the current month
                monthly_total += price
                monthly_count += 1

    # Display the last month's average
    monthly_average = monthly_total / monthly_count
    monthly_name = monthList[current_month - 1]
    print(f"{monthly_name:>20}\t{monthly_average:>20,.2f}")


def main():
    while True:
        # Try block to check to validade user input
        try:
            filename = input("Enter the DJIA closing price file name: ")
            dateList, priceList = readFile(filename)
            displayOutput(dateList, priceList)
            break
        except FileNotFoundError as err:
            print(f"File not found: {err}")
        except IOError as err:
            print(f"Error reading the file: {err}")

# Call main
if __name__ == "__main__":
    main()
