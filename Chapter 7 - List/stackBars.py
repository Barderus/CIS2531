'''
Authr: Gabriel dos Reis
Date: 10/22023
Purpose: Represent  the credit students by status using matplot library. Practice of using stackbar.
'''

import matplotlib.pyplot as plt

def main():
    # Create a list with the x coordinates of each bar's left edge
    x_labels = ["2015", "2016", "2017", "2018", "2019"]
    left_edges = [0, 10, 20, 30, 40]
    
    # Create a list with the height of each bar
    FT_height = [9811, 9004, 8510, 7857, 7793]
    PT_height = [18867, 17897, 17655, 17043, 16110]
    
    # Create a variable for the bar width
    bar_width = 8
    
    # Add a title
    plt.title("Credit Student by Status")
    
    # Add labels to the axes
    plt.xlabel("Year")
    plt.ylabel("Students")
    
    # Build the bar chart
    plt.bar(left_edges, PT_height, bar_width, color="b", edgecolor ="k",
            label = "Part time < 12hrs")
    plt.bar(left_edges, FT_height, bar_width, color="g",
            edgecolor = "k", label="Full time >= 12 hrs", bottom=PT_height)
    
    # Customize the tick marks
    plt.xticks(left_edges, x_labels)
    plt.yticks([5000, 10000, 15000, 20000, 25000, 30000], 
               ["5k", "10k", "15k", "20k", "25k", "30k"])
    
    # Add a legend at best location
    plt.legend()
    
    # Display the line graph
    plt.show()
    
main()
