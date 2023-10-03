'''
Author: Gabriel dos Reis
Date: 10/03/2023
Program: DMV_exam.py
Purpose: Write a modular program that reads the file of a student DMV answers and compare to the correct answers. The program must compute and display
how many answers the student got right and how many the student got wrong. Then, the program should display a pie chart showing the percentage of
correct and incorrect answers.
'''

# Import Matplotlib library
import matplotlib.pyplot as plt

# Named constant
PASS = 15

# Function to read student answers from a file into a list and return the list.
def read_answers():
    while True: # Loop to run until a valid file is entered
        student_answers = []
        # Open file
        try:
            filename = input("Enter file name: ")
            infile = open(filename, "r")
        except FileExistsError as err:
            print(err)
        except FileNotFoundError as err:
            print(err)
        except IOError as err:
            print(err)
        else:
            
            # Strip whitespace
            for line in infile:
                student_answers.append(line.strip())
        break
    return student_answers

def compare_answers(correct_answers, student_answers):
    correct_indices = []
    incorrect_indices = []
    
    # Count
    correct_count = 0
    incorrect_count = 0
    
    # Loop to compare each line of the file with the correct answer's tuple
    for i in range(len(correct_answers)):
        if student_answers[i].upper() == correct_answers[i]:
            correct_count += 1
            correct_indices.append(i+1)
        else:
            incorrect_count += 1
            incorrect_indices.append(i+1)
    return correct_indices, incorrect_indices

def pieChart(correct_count, incorrect_count):
    
    # Create a list with the data aquired from main
    headCount = [correct_count, incorrect_count]
    slice_labels = ["Correct answers", "Incorrect"]
    
    # Create a pie chart from the values
    plt.pie(headCount, labels=slice_labels, autopct="%.0f%%")
    
    # Add a title    
    plt.title("DMV Exam Results")
    
    plt.show()
    

def main():
    # Create a tuple to hold the correct answers
    correct_answers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", 
                    "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
    student_answers = read_answers()
    #compare_answers(correct_answers, student_answers)
    correct_indices, incorrect_indices = compare_answers(student_answers, correct_answers)
    
    # Count correct and incorrect answers
    correct_count = len(correct_indices)
    incorrect_count = len(incorrect_indices)
    
    # Display a congrutalotory message if the student got 15 or more answers correct
    if correct_count >= PASS:
        print("\nCongratulations! You passed the exam.")
        print(f"Number of questions answered correctly: {correct_count}")
        if correct_count > 0:
            print("Questions: ", end="")
            for i in range(len(correct_indices)):
                print(correct_indices[i], end="")
                if i < len(correct_indices) - 1:
                    print(", ", end="")
        print()
        print(f"\nNumber of questions you answered incorrectly:  {incorrect_count}")
        if incorrect_count > 0:
            print("Questions: ", end="")
            for i in range(len(incorrect_indices)):
                print(incorrect_indices[i], end="")
                if i < len(incorrect_indices) - 1:
                    print(", ", end="")

                        
    # Message if the user got less than 15 answers incorrect       
    else:
        print("\nSorry, you did not pass the exam.")
        print()
        print(f"Number of questions you answered correctly: {correct_count}")
        if correct_count > 0:
            print("Questions: ", end="")
            for i in range(len(correct_indices)):
                print(correct_indices[i], end="")
                if i < len(correct_indices) - 1:
                    print(", ", end="")
        print(f"Number of questions you answered incorrectly:  {incorrect_count}")
        if incorrect_count > 0:
            print("Questions: ", end="")
            for i in range(len(incorrect_indices)):
                print(incorrect_indices[i], end="")
                if i < len(incorrect_indices) - 1:
                    print(", ", end="")
    
    pieChart(correct_count, incorrect_count)
    
if __name__ == "__main__":
    main()
    
''' *** SAMPLE OUTPUT ***
nter file name: answers.txt

Congratulations! You passed the exam.
Number of questions answered correctly: 18
Questions: 1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20

Number of questions you answered incorrectly:  2
Questions: 3, 11
'''