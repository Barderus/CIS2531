FIELD_DELIMITER = ","

def readFile(filename):
    dateList = []
    priceList = []
    
    infile = open(filename, "r")
    for line in infile:
        field_list = line.strip().split(FIELD_DELIMITER)
        date, price = field_list
        dateList.append(date)
        priceList.append(float(price))
    infile.close()
    return dateList, priceList

def calculateMonthAverages(dateList, priceList):
    month_totals = [0] * 12
    month_counts = [0] * 12

    for date, price in zip(dateList, priceList):
        month = int(date.split("/")[0])  # Extract the month (MM/DD/YYYY)
        month_totals[month - 1] += price  # Adjust for 0-based indexing
        month_counts[month - 1] += 1

    average_prices = [0] * 12
    for i in range(12):
        if month_counts[i] > 0:
            average_prices[i] = month_totals[i] / month_counts[i]

    return average_prices

def displayOutput(dateList, priceList):
    message = "DJIA closing price averages for"
    monthMsg = "MONTH"
    avgMsg = " AVERAGE"
    delimiterMsg = "====="
    monthList = ["January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]
    previousYear = None

    print(f"{message}\n{monthMsg:>30}\t{avgMsg:>30}\n{delimiterMsg:>30}\t{delimiterMsg:>30}")

    for date, price in zip(dateList, priceList):
        month, _, year = date.split("/")
        month = int(month)
        year = int(year)
        monthStr = monthList[month - 1]

        if year != previousYear:
            print(f"{message} {year}")
            previousYear = year

        print(f"{monthStr:>30}\t{price:>30}")

    # Calculate and display monthly averages
    monthly_averages = calculateMonthAverages(dateList, priceList)
    for i in range(12):
        print(f"{monthList[i]:>30}\t{monthly_averages[i]:>30}")

def main():
    while True:
        try:
            filename = input("Enter the DJIA closing price file name: ")
            dateList, priceList = readFile(filename)
            displayOutput(dateList, priceList)
            break
        except FileNotFoundError as err:
            print(f"File not found: {err}")
        except IOError as err:
            print(f"Error reading the file: {err}")

if __name__ == "__main__":
    main()
