'''
Author: Gabriel dos Reis
Date: 10/17/2023
Program: uniqueWords.py
Description: Get an input paragraph from the usr and identify the unique words
'''

def main():
    
    # Get the paragraph from the user
    paragraph = input("Enter a paragraph: ")
    
    # Split the paragraph into a list of words
    words = paragraph.split()
    
    # Create a set of unique words
    uniqueWords = set(words)
    
    # Print the unique words
    print("There are", len(words), "words in the paragraph.")
    print("There are", len(uniqueWords), "unique words in the paragraph.")
    print("The unique words are: ")
    for word in uniqueWords:
        print(word, end=" ")
    

# Call the main function to start
if __name__ == "__main__":
    main()