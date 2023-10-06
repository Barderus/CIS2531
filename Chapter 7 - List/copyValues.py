'''
Assume the list numbers1 has 100 elements, and numbers2 is an empty list. Write code that copies the values in numbers1 to numbers2.
'''

def main():
    
    # List of 100 numbers
    numbers1 = [n for n in range(1,101)]
    
    # Copy the numbers1 list to numbers2 list
    numbers2 = numbers1.copy()
    
    #print(numbers1)
    #Clear numbers1
    numbers1.clear()
    print(numbers2)
    print("Numbers1 list: ", numbers1)

if __name__ == "__main__":
    main()