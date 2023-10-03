'''
Pie chart
'''
import matplotlib.pyplot as plt

def main():
    
    # Create a list of head counts for given year across age ranges
    headCount = [5732, 10745, 6635, 791]
    
    slice_labels = ["HS Grads (<= 18)", "Young Adults (19-24)", "Adults (25-54)", "Older adults (> 55)"]
    # Create a pie chart from the values
    plt.pie(headCount, labels=slice_labels, autopct="%.0f%%")
    
    # Add a title    
    plt.title("Credit Students by Ange Range for 2019")
    
    plt.show()

main()