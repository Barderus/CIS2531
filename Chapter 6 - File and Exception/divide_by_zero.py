def main():
    while True:
        try:
            # Get two numbers
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            
            # Divide the numbers by num1 and num2 and display the result
            result1 = num1 / num2
        except ValueError:
            print("Please enter a valid number")
        except ZeroDivisionError as e:
            print(e)
        else:
            print(f"{num1} divided by {num2} is {result1}")
            break

    print("Division completed")

# Call the main function
if __name__ == "__main__":
    main()
