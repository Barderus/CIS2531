'''
Write a code that opens an output file with the filename number_list.txt,
but does not rease the file's contents if it already exists.
'''

def main():
    
    # Filename
    filename = "number.list.txt"
    
    try:
        infile = open(filename, "r")
    except IOError as e:
        print(e)            
    else:
        
        for line in infile:
            print(int(line))
        infile.close()

main()