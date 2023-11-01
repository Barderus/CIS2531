'''
cellphone_test.py
'''
from Cellphone import Cellphone

def main():
    

    # Get the phone data
    manufacturer = input("Enter the cellphone's manufacturer: ")
    model = input("Enter the cellphone's model number: ")
    retail = float(input("Enter the cellphone's retail price: "))

    # Create an instance
    cellphone1 = Cellphone(manufacturer, model, retail)
    #cellphone2 = Cellphone(manufacturer, model, retail)
    #cellphone3 = Cellphone(manufacturer, model, retail)
    
    # Display the data that was entered
    print(f"Manufacturer: {cellphone1.get_manufacturer()} \tModel Number: {cellphone1.get_model_num()} \tRetail Price ${cellphone1.get_retail_price()}")
    #print(f"Manufacturer: {cellphone2.get_manufacturer} \tModel Number:{cellphone2.get_model_num} \tRetail Price{cellphone2.get_retail_price}")
    #print(f"Manufacturer: {cellphone3.get_manufacturer} \tModel Number:{cellphone3.get_model_num} \tRetail Price{cellphone3.get_retail_price}")


if __name__ == "__main__":
    main()
