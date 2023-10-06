'''
Write a statement that creates a list with the following strings: 'Einstein', 'Newton', 'Copernicus', and 'Kepler'. 
Assume names references a list. Write a for loop that displays each element of the list.
'''

def main():
    
    # List of names
    name_list = ["Einstein", "Newton", "Copernicus", "Kepler"]    
    
    # Loop to go through the list and print the info
    for i in range(len(name_list)):
        print(name_list[i])
        
if __name__ == "__main__":
    main()