'''
Write a program that opens the number_list.txt adn reads all the numbers from the file
and displays them. Then, adds all of the numbers read and display the total.
'''

def main():
    
    #Accumulator
    count = 0
    
    # Filename
    filename = "number_list.txt"
    
    # Open file for read
    infile = open(filename, "r")
    
    #Reads the file
    for line in infile:
        # Convert the numbers to ineger
        numbers = int(line)
        print(numbers)
        count += numbers
    print("The sum of all numbers of the file is", count)
    
    #Close the file
    infile.close()
    
main()
        