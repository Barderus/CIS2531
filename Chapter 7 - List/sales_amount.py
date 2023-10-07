'''
Design a program that asks the user to enter a store’s sales for each day of the week. 
The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.
'''
import matplotlib.pyplot as plt

DAYS_OF_WEEK = 7

def bar_chart(sales_list):
    # Create a list with the x coordinates of each bar's left edge
    x_labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    #left_edges = [100, 200, 300, 400, 500, 600, 700]
    
    
    # Create a list with the height of each bar
    heights = sales_list.copy()
    
    # Create a variable for the bar width
    bar_width = 8
   
    # Add a title
    plt.title("Total sales of the week")
    
    # Add labels to the axes
    plt.xlabel("Sales")
    plt.ylabel("Weekdays")
     
    # Build the bar chart
    plt.bar(x_labels, heights, color=("b", "g", "r", "m", "y", "k", "c"))
    
    # Display the bar graph
    plt.show()
    
def main():
    
    total = 0
    
    sales_list = []
    #  Need to add try block for input validation
    for days in range(1,(DAYS_OF_WEEK+1)):
        if days == 1:
            sales = float(input("How much did you sell on Monday?:  "))
        if days == 2:
            sales = float(input("How much did you sell on Tuesday?:  "))
        if days == 3:
            sales = float(input("How much did you sell on Wednesday?:  "))
        if days == 4:
            sales = float(input("How much did you sell on Thursday?:  "))
        if days == 5:
            sales = float(input("How much did you sell on Friday?:  "))
        if days == 6:
            sales = float(input("How much did you sell on Saturday?:  "))
        if days == 7:
            sales = float(input("How much did you sell on Sunday?:"))
        sales_list.append(sales)
    for num in sales_list:
        total += num
    print(f"The total this week was: {total:.2f}")

    bar_chart(sales_list)

if __name__ == "__main__":
    main()