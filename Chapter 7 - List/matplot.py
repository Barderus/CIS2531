'''
Author: Gabriel dos Reis
Date: 10/2/2023
Purpose: Credit student by gender graph.
'''

import matplotlib.pyplot as plt

def main():
    
    # Create list with X and Y coordinates of each point
    x_coord = [0, 1, 2, 3, 4]
    x_labels = ["2015", "2016", "2017", "2018", "2019"]
    y_female = [9811, 9004, 8510, 7857, 7793]
    y_male = [18867, 17897, 17655, 17043, 16110]
    y_unkown = [0, 0, 0, 0, 219]
    
    # Add a title
    plt.title("Credit student by Gender")
    
    # Add labels to the axes
    plt.xlabel("Year")
    plt.ylabel("Students")
    
    # Add a grid
    plt.grid(True)
    
    # Build the line graph
    # Using marker, colors, and legend labels
    plt.plot(x_coord, y_female, marker="o", color="r", label="female")
    plt.plot(x_coord, y_male, marker="s", color="b", label="Male")
    plt.plot(x_coord, y_unkown, marker="D", color="xkcd:purple", label="Unkown")
    
    # CUstomize the tick marks
    plt.xticks(x_coord, x_labels)
    plt.yticks([5000, 8000, 11000, 14000, 17000, 20000], 
               ["5k", "8k", "11k", "14k", "17k", "20k"])
    
    # Add a legend at best location
    plt.legend()
    
    # Display the line graph
    plt.show()
    
main()
