'''
Write a program that prompts the user for the number of stocks records to file.
Also, prompt the user for the filename and data for each stock
record.
    Ticket symbol --> character string
    Company name --> character string
    YTD percent change --> integer number
    closing price --> floating point number
'''

# Named constant
FIELD_DELIMITER = ':'

def main():
    num_stocks = int(input('Enter the number of stocks: '))
    filename = input('Enter the filename: ')
    
    # Open the file for writing
    outfile = open(filename, 'w')

    # Read stock data from user and write data to fike
    for i in range(num_stocks):
        # Prompt and read stock details from user.
        print('Enter the details of stock #', i + 1, sep='')
        ticket = input('Enter the symbol: ')
        company_name = input('Enter the name: ')
        ytd_perfor = int(input('Enter the YTD: '))
        closing_price = float(input('Enter the closing price: '))

        # Create a delineated record of stock data
        stock_str = ticket + FIELD_DELIMITER + company_name + FIELD_DELIMITER + str(ytd_perfor) + FIELD_DELIMITER + str(closing_price)
        
        # Write record out to file
        outfile.write(stock_str + "\n")
        
    # Close the file
    outfile.close()
    print("Records written to", filename + ".")
    
main()