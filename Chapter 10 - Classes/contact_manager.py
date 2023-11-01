'''
Contact Manager
Next, you could write a program that keeps  objects in a dictionary. Each time the program creates an object holding a specific person’s data, 
that object would be stored as a value in the dictionary, using the person’s name as the key. 
Then, any time you need to retrieve a specific person’s data, you would use that person’s name as a key to retrieve the  object from the dictionary
The program displays a menu that allows the user to perform any of the following operations:
                
    * Look up a contact in the dictionary
    * Add a new contact to the dictionary
    * Change an existing contact in the dictionary
    * Delete a contact from the dictionary
    * Quit the program
'''

from Contact import Contact
import pickle

# Global constants for menu
LOOKUP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILENAME = "contacts.dat"

def load_contacts():
    try:
        # Open the contacts.dat file
        input_file = open(FILENAME, "rb")
        
        #Unpickle the dictionary
        contact_dct = pickle.load(input_file)
        
        #Close the phone_inventory.dat file
        input_file.close()
    except IOError:
        # Could not open the file, so create an empty dictionary
        contact_dct = {}
    # Return the dictionary
    return contact_dct

# Function that displays the menu choices availables and prompt the user for user's choice.
    #Then it returns the user's choice
def get_menu_choice():
    print("\nEnter: \n\t1. to LOOK UP a contact.\n\t2. to add a NEW contact.\n\t3. to CHANGE a contact.\n\t4. to DELETE your contact.\n\t5. to QUIT the progrm")
    menu_choice = int(input("Enter your option: "))
    
    #Validade the user's choice
    while menu_choice < LOOKUP or menu_choice > QUIT:
        menu_choice = int(input("Enter a valid choice: "))
    
    # Return the user's choice
    return menu_choice

# Look-up function to look up an item in the dictionary
def look_up(my_contacts):
    # Get a name to look up
    name = input("Enter a name: ")
    
    # Look it up in the dictionary
    print(my_contacts.get(name, "That name is not found."))

# This function adds a new entry into the dictionary    
def add(my_contacts):
    # Get the contact info
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    
    #Create a Contact object named entry
    entry = Contact(name, phone, email)
    
    # If the name does not exist in the dictionary, add it as a key with the entry
    # object as the associated value
    if name not in my_contacts:
        my_contacts[name] = entry
        print("The contact has been added.")
    else:
        print("That name alredy exists.")

# The change function changes an existing contact in the dictionry        
def change(my_contacts):
    
    # Get a name to look up
    name = input("Enter a name: ")
    
    if name in my_contacts:
        # Get a phone number
        phone = input("Enter the new phone number: ")
        
        # Get a new email address
        email = input("Enter the new email: ")
        
        # Create a contact oject named entry
        entry = Contact(name, phone, email)
        
        # Update the entry
        my_contacts[name] = entry
        print("Information updated.")
    else:
        print("That name is not found.")

# This functin allows the user to delete an entry from the dictionary    
def delete(my_contacts):
    
    # Get a name to look up
    name = input("Enter a name: ")
    
    #If the name is found, then delete the entry
    if name in my_contacts:
        del my_contacts[name]
        print("Contact deleted.")
    else:
        print("That name is not found")

# Save contact function pickles the specified object and saves it to the contacts file
def save_contacts(my_contacts):
    
    #Open the file for writing
    output_file = open(FILENAME, "wb")
    
    # Pickle the dictionary and save it
    pickle.dump(my_contacts, output_file)
    
    # Close the file
    output_file.close()

def main():
    # Load the existing contact dictionary and assign it to my contacts
    my_contacts = load_contacts()
    
    # Initialize a variable for the user's choice
    choice = 0
    
    # Process enu selections until the user wnats to quit
    while choice != QUIT:
        # Get the user's menu choice
        choice = get_menu_choice()
        
        # Process the choice
        if choice == LOOKUP:
            look_up(my_contacts)
        elif choice == ADD:
            add(my_contacts)
        elif choice == CHANGE:
            change(my_contacts)
        elif choice == DELETE:
            delete(my_contacts)
    # Save the mycontacts dictionary to a file
    save_contacts(my_contacts)

# Call main and run the program   
if __name__ == "__main__":
    main()