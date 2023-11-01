'''
This program creates five CellPhone objects and stores them in a list
'''
from Cellphone import Cellphone

def main():
    # Get a list of CellPhone Objects
    phones = make_list()
    
    #Display the data in the list
    display_list(phones)
    

'''
The make_list function gets data from the user for five phones.
The function returns a list of cellphones objects containing the data
'''
def make_list():
    # create an empyty list
    phone_list = []
    
    # Add five CellPhone objects to the list.
    for count in range(1,6):
        # Get the phone data
        print("Phone number", str(count), ":")
        manufacturer = input("Enter the manufactor: ")
        model_num = input("Enter the mmodel number: ")
        retail_price = float(input("Enter the retail price: "))
        
        # Create a new CellPhone object in memory and assign it to the phone variable
        phone = Cellphone(manufacturer, model_num, retail_price)
        
        # Add the object to the list
        phone_list.append(phone)
    return phone_list

'''
    The display_list function accepts a list containing Cellphone objects
    as an argument and displays the data stored in each object
'''

def display_list(phone_list):
    print("List of Phones:")
    for item in phone_list:
        
        print("\tManufacturer: ", item.get_manufacturer())
        print("\tModel: ", item.get_model_num())
        print("\tRetail price: $", item.get_retail_price())
        print()

if __name__ == "__main__":
    main()
        
    
    
    