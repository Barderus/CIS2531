'''
Driver's license Exam
'''

def main():
    correct_answers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", 
                       "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]

    student_answers = []  # Initialize a list to store student answers
    incorrect_indices = []  # Initialize a list to store incorrect answer indices

    # Read student answers from a file
    with open("answers.txt", "r") as infile:
        for line in infile:
            student_answers.append(line.strip())

    # Check student answers against correct answers
    correct_count = 0
    incorrect_count = 0

    for i in range(len(correct_answers)):
        if student_answers[i].upper() == correct_answers[i]:
            correct_count += 1
        else:
            incorrect_count += 1
            incorrect_indices.append(i + 1)  # Adding 1 to get the question number

    # Determine if the student passed or failed
    if correct_count >= 15:
        pass_fail_status = "Passed"
    else:
        pass_fail_status = "Failed"

    # Display the results
    print(f"Pass/Fail Status: {pass_fail_status}")
    print(f"Total Correct Answers: {correct_count}")
    print(f"Total Incorrect Answers: {incorrect_count}")
    print(f"Incorrect Answer Question Numbers: {incorrect_indices}")

if __name__ == "__main__":
    main()
 