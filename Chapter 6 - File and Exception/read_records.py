'''
Prompt the user for the file name and get the following data from each file line:
    Ticket symbol
    Company name
    YTD percentage change
    Closing price
Displa
'''
# Named constant
FIELD_DELIMITIER = ":"
TICKER_WIDTH = 20
CMP_WIDTH = 10
YTD_WIDTH = 20
PRICE_WIDTH =20

def main():
    # Get file name from user
    file_name = input("Enter file name: ")
    
    # Counter for number of records
    num_stk = 0
    #Accumulator to keep track of total YTD
    total_ytd = 0
    
    '''
    Display String formatted with column headers
        -> 10 characters for ticker symbol
        -> 30 characters for company name
        -> 10 characters for YTD percent (right aligned)
        -> 10 characters for price(right aligned)
        
    '''

    
    
    #Open the file for reading
    infile = open(file_name, 'r')
    
    # Read each line until no more records
    for line in infile:
        # Increment stock counter
        num_stk += 1
        # Split out individual fields from line/record
        field_list  = line.split(FIELD_DELIMITIER)
        
        # parse each field as item in list
        ticker = field_list[0]
        company_name = field_list[1]
        ytd_percent_change = int(field_list[2])
        closing_price = float(field_list[3])
        
        # Accumulate the YTD percent
        total_ytd += ytd_percent_change
        
        # Display data in columnar format
        print(str(format(ticker, str(TICKER_WIDTH) + "s") + 
              format(company_name, str(CMP_WIDTH) + "s") + 
              format(ytd_percent_change, ">"+ str(YTD_WIDTH) + "d") + 
              format(closing_price, ">" + str(PRICE_WIDTH) + ".2f")))
        
    # Display the summary statistics
    print("Total number of stocks read from file =", num_stk)
    print("With average YTD percent =", format(total_ytd/num_stk, ".2f"))

# Start program by calling main function
main()
        
