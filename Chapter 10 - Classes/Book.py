'''
Author: Gabriel dos Reis
Date: 11/1/2023
Program: Book.py
Purpose:
Write a class definition named Book. 
The Book class should have data attributes for a book’s title, the author’s name, and the publisher’s name. 
The class should also have the following: 
    • An _ _init_ _ method for the class. The method should accept an argument for each of the data attributes. 
    • Accessor and mutator methods for each data attribute. 
    • An _ _str_ _ method that returns a string indicating the state of the object
'''

class Book():
    def __init__(self, title, author, publisher):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        
    # Setters
    
    def set_title(self, title):
        self.__title = title
    
    def set_author(self, author):
        self.__author = author
        
    def set_publisher(self, publisher):
        self.__publisher = publisher
    
    # Getters
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_publisher(self):
        return self.__publisher
    
    # __str__ that returns a string indicating the object
    def __str__(self):
        book_atr = f"Book title: {self.__title}\tBook author: {self.__author}\tBook publisher: {self.__publisher}"
        
        return book_atr