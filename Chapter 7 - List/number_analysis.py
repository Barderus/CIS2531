'''
Design a program that asks the user to enter a series of 20 numbers. 
The program should store the numbers in a list then display the following data:
The lowest number in the list 
The highest number in the list 
The total of the numbers in the list 
The average of the numbers in the list

'''
NUMBER_LIMIT = 20

def lowest(num_list):
    # Set the lowest value as the first index of the list
    # If the lowest[n] has a smaller value than the lowest, assign that value to lowest
    lowest = num_list[0]
    for n in range(len(num_list)):
        if lowest > num_list[n]:
            lowest = num_list[n]
    return lowest
    
def highest(num_list):
    # Set the highest value as the first index of the list
    # If the highest[n] has a smaller value than the highest, assign that value to highest
    
    highest = num_list[0]
    for n in range(len(num_list)):
        if highest < num_list[n]:
            highest = num_list[n]
    return highest

def average(num_list):
    # Set total to 0
    # Each iteration adds the value of that index to total, then divides it by the length of the num_list
    total = 0
    for n in range(len(num_list)):
        total += num_list[n]
    return total / len(num_list)
    
def total(num_list):
    # Set total to 0
    # Each iteration adds the value of that index to total, returns total
    total = 0
    for n in range(len(num_list)):
        total += num_list[n]
    return total

def main():
    
    # Initialize the num list
    nums = []
    
    # Try block to prompt user for numbers and append it to the user_num list.  It checks for characters, and negative numbers
    for i in range(0, NUMBER_LIMIT):
            while True:
                try:
                    user_num = float(input(f"Enter {i+1} number of the list: "))
                    if user_num >= 0:
                        break
                except ValueError as err:
                    print(err)
                else:
                    nums.append(user_num)
    # Call the functions to find the lowest number, highest number, average number, and the total   
    lowest_num = lowest(nums)
    highest_num = highest(nums)
    avg_num = average(nums)
    ttl_num = total(nums)
    
    # Display the result
    print(f"The lowest value number is {lowest_num}")
    print(f"The highest value number is {highest_num}")
    print(f"The average value number is {avg_num}")
    print(f"The total sum of the list is {ttl_num}")

# Call the main function          
if __name__ == "__main__":
    main()