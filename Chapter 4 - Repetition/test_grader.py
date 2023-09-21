def letter_grader(test):
    if test >= 90:
        return "A"
    elif test >= 80:
        return "B"
    elif test >= 70:
        return "C"
    elif test >= 60:
        return "D"
    else:
        return "F"


def average_grade(test_ttl):
    average = test_ttl / 5
    return average

def main():
    print("Enter the grade of 5 tests")
    print()
    accumulator = 0

    for t in range(1,6):
        test_input = float(input(f"Enter test grade {t}: "))
        accumulator += test_input
        letter = letter_grader(test_input)
        print(f"The letter grade for test {t} is", letter)
        print()
    print(f"The average score is", average_grade(accumulator))

main()
