'''
Print the following pattern 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
ROW = 5
for r in range(0, ROW):
    for c in range(0, r+1):
        print(c+1, " ", end="")
    print()
    
'''
'ROW' is a name constant that sets the maximum number of rows.
'for r in range(0, ROW)' Outer loop that iterates from 0 to ROW-1 (4). Each iteration creates a row(5 rows total)
'for c in range(0, r+1)' Inner loop that iterates from 0 to r+1(5).
'print(c+1, " ", end="")" Prints the incremental value of c(starting at 0 til 4), with a space between the numbers
and it makes sure to remove any possible new line so they all print in the same line
'print()' goes to the next line for each iteration


'''