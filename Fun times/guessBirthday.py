'''
Guess someone's birthday within 5 question
'''

def main():
    
    set1 = [1, 3, 5, 7,  9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    set2 = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 22, 23, 26, 27, 30, 31]
    set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
    set4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
    set5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    
    day = 0
    
    print("Hello! I'm going to guess your birthday in 5 or less question... Are you ready?")
    
    # First question
    print("First question: \nIs your birthday in any of these numbers?")
    for num in set1:
        print(num, end=" ")
        
    answer = input("\nyes / no: ")
    
    if answer.lower() == "yes":
        day += 1
        
    # Secod question
    print("\nSecond question: \nIs your birthday in any of these numbers?:")
    for num in set2:
        print(num, end=" ")
    answer = input("\n yes / no?: ")
    print("\n\t Hmm, interesting...")

    
    if answer.lower() == "yes":
        day += 2
        
    # Third question
    print("\nThird question: \nIs your birthday in any of these numbers?:")
    for num in set3:
        print(num, end=" ")
    answer = input("\nyes / no?: ")
    
    if answer.lower() == "yes":
        day +=4
        
    # Fourth Question
    print("\nFourth Question: \nIs your birthday in any of these numbers?:")
    for num in set4:
        print(num, end=" ")
    answer = input("\nyes / no?: ")
    print("\n\tThat's so peculiar!")
    
    if answer.lower() == "yes":
        day += 8
        
    # Fifth question
    print("\nFifth question: \nIs your birthday in any of these numbers?:")
    for num in set5:
        print(num, end=" ")
    answer = input("\nyes / no?: ")
    
    if answer.lower() == "yes":
        day += 16
    print("\n\tHA! I believe I got it!") 
    print(f"Your birth day...\n\tis on...\n\t\t {day}!")
 
main()