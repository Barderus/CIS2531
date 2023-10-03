'''
Write on the file
'''

def main():
    
    filename = "answers.txt"
    
    outfile = open(filename, "w")
    
    answers1 = ["A", "C", "D", "A", "D", "B", "C", "A", "C", "B", 
                       "B", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
    
    for items in answers1:
        outfile.write(f"{items}\n")
    
main()
