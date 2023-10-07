'''
A positive integer greater than 1 is said to be prime if it has no divisors other than 1 and itself. 
A positive integer greater than 1 is composite if it is not prime. 
Write a program that asks the user to enter an integer greater than 1, then displays all of the prime numbers that are less than or equal to the number
entered. The program should work as follows:
    Once the user has entered a number, the program should populate a list with all of the integers from 2 up through the value entered. 
    The program should then use a loop to step through the list. 
    The loop should pass each element to a function that displays whether the element is a prime number, or a composite number.

'''

def is_prime(list_nums):
    
    
def main():
    
    num_limit = int(input("Enter the number limit: "))
    
    list_nums = [n for n in range(1,num_limit+1)]
    
    is_prime(list_nums)
    

if __name__ == "__main__":
    main()