'''
'''
# Import Matplot library
import matplotlib.pyplot as plt

# Named constant
PASS = 15

# Function that handles the pie chart. It receives two arguments, the number of correct answers, and the number of incorrect answers.
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
        
    # Create a list to hold the student answers and the indices of the student correct/incorrect answers
    student_answers = []
    correct_indices = []
    incorrect_indices = []
    
    
    while True: # Loop to run until a valid file is entered
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
            
            # Display a congrutalotory message if the student got 15 or more answers correct
            if correct_count >= PASS:
                print("\nCongratulations! You passed the exam.")
                print(f"Number of questions answered correctly: {correct_count}")
                if correct_count > 0:
                    print("Questions: ", end="")
                    for i in correct_indices:
                        print(i, end=", ")
                print(f"\nNumber of questions you answered incorrectly:  {incorrect_count}")
                if incorrect_count > 0:
                    print("Questions: ", end="")
                    for i in incorrect_indices:
                        print(i, end=", ")
                        
            # Message if the user got less than 15 answers incorrect       
            else:
                print("\nSorry, you did not pass the exam.")
                print(f"Number of questions you answered correctly: {correct_count}")
                if correct_count > 0:
                    print("Questions: ", end="")
                    for i in correct_indices:
                        print(i, end=", ")
                print(f"\nNumber of questions you answered incorrectly:  {incorrect_count}")
                if incorrect_count > 0:
                    print("Questions: ", end="")
                    for i in incorrect_indices:
                        print(i, end=", ")
            # Close the file
            infile.close()
            # End loop
            break
    
    # Call pie chart function
    pieChart(correct_count, incorrect_count)
        
    

if __name__ == "__main__":
    main()
    
''' *** Sample output 
*** 
'''
    
