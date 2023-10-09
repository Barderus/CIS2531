'''
A positive integer greater than 1 is said to be prime if it has no divisors other than 1 and itself. 
A positive integer greater than 1 is composite if it is not prime. 
Write a program that asks the user to enter an integer greater than 1, then displays all of the prime numbers that are less than or equal to the number
entered. The program should work as follows:
    Once the user has entered a number, the program should populate a list with all of the integers from 2 up through the value entered. 
    The program should then use a loop to step through the list. 
    The loop should pass each element to a function that displays whether the element is a prime number, or a composite number.

'''
import math

# Function that checks if the number is prime
# Number cannot be less than 1, and if can be divided by 2 or the sqr of it, it's not prime
# Otherwise, it returns true
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    
def main():
    # Prompt user for number limit
    num_limit = int(input("Enter the number limit: "))
    
    # Populate the list fom 1 to the number entered
    list_nums = [n for n in range(1,num_limit+1)]
    
    # Display the prime numbers
    print("Prime numbers: ", end="")    
    for num in list_nums:
        if is_prime(num):
            print(f"{num} ",end="")
    
    # Display the composite numbers
    print("\nComposite numbers: ", end="")
    for num in list_nums:
        if is_prime(num) == False:
            print(f"{num} ", end="")
    

if __name__ == "__main__":
    main()