'''
Expense Pie Chart
Create a text file that contains your expenses for last month in the following categories:
    Rent 
    Gas 
    Food 
    Clothing 
    Car payment 
    Misc 
'''
import matplotlib.pyplot as plt

def pieChart():
    # Create a list of head counts for given year across age ranges
    headCount = [5732, 10745, 6635, 791]
    
    slice_labels = ["Gas", "Clothing", "Food", "Miscellaneous"]
    # Create a pie chart from the values
    plt.pie(headCount, labels=slice_labels, autopct="%.0f%%")
    
    # Add a title    
    plt.title("Expenses of the month")
    
    plt.show()

def writeGas(file):
    
    outfile = open(file, "w")
    
    gasSpnt = float(input("Enter the amount of gas spent: "))
    outfile.write(str(gasSpnt + "\n"))
    
    outfile.close()

    
def writeClothing(file):
    
    outfile = open(file, "w")
    
    clothingSpnt = float(input("Enter the amount spend with clothing: "))
    outfile.write(str(clothingSpnt + "\n"))
    
    outfile.close()
    
def writeFood(file):
    
    outfile = open(file, "w")
    
    foodSpnt = float(input("Enter the amount of food spent: "))
    outfile.write(str(foodSpnt + "\n"))
    
    outfile.close()


def writeMisc(file):
    
    outfile = open(file, "w")
    
    miscSpnt = float(input("Enter the amount of miscellaneous spent: "))
    outfile.write(str(miscSpnt + "\n"))
    
    outfile.close()
    
def menu():
    
    userInput = int(input("Choose: ",
          "1. Gas Spendings",
          "2. Clothes Spending",
          "3. Food Spending",
          "4. Miscellaneous Spending",
          "5. Clear files",
          "6. Exit"))
    return userInput
       
def main():
    
    gasFile = "gas.txt"
    clothingFile = "clothing.txt"
    foodFile = "food.txt"
    miscFile = "misc.txt"
    
    userChoice = menu()
    
    if userChoice == 1:
        writeGas(gasFile)
    elif userChoice == 2:
        writeClothing(clothingFile)
    elif userChoice == 3:
        writeFood(foodFile)
    elif userChoice == 4:
        writeMisc(miscFile)
    elif userChoice == 5:
        # Clear everything in the file
    elif userChoice == 6:
        exit()
    else:
        print("ERROR!")
        
    pieChart()
    
if __name__ == "__main__":
    main()