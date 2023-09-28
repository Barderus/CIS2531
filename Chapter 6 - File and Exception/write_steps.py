'''
Create a file with 365 lines, each line with the number of steps on that day
'''
DAYS = 365
def main():
    
    # Filename
    filename = "steps.txt"
    
    #Open file
    outfile = open(filename, "w")
    
    for d in range(DAYS):
        step_day = int(input("Number of steps: "))
        
        outfile.write(str(step_day) + "\n")
    outfile.close()
    
main()
    