'''
Matplot bar function
Author: Gabriel dos Reis
Date: 10/2/2023
Purpose: Using Matplot library to plot a bar graph based on the data of the total credit student by year. Practice bar graph.
'''

import matplotlib.pyplot as plt

def main():
    
    # Create a list with the x coordinates of each bar's left edge
    x_labels = ["2015", "2016", "2017", "2018", "2019"]
    left_edges = [0, 10, 20, 30, 40]
    
    # Create a list with the height of each bar
    heights = [28678, 26901, 26165, 24900, 23903]
    
    # Create a variable for the bar width
    bar_width = 8
   
    # Add a title
    plt.title("Total Credit Student by Year")
    
    # Add labels to the axes
    plt.xlabel("Year")
    plt.ylabel("Students")
     
    # Build the bar chart
    plt.bar(left_edges, heights, bar_width, color=("r", "g", "b", "y", "k"))
    
    # CUstomize the tick marks
    plt.xticks(left_edges, x_labels)
    plt.yticks([20000, 22000, 24000, 26000, 28000, 30000], 
               ["20k", "22k", "24k", "26k", "28k", "30k"])
    
    # Set y axis limits
    plt.ylim(bottom=20000)
    
    # Display the bar graph
    plt.show()

main()