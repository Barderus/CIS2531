'''
    Program to use CashRegister object to make
    RetailItem purchases.  Includes looping menu
    display, user selection of items for purchase,
    checkout, and total calculations.
    **copyright CREngland, COD
'''
import RetailItem as r
import CashRegister as cr

def menuChoice(ritems):
    # display items for purchase
    print('\nItems Available for Purchase')
    print('----------------------------')
    print()
    print(f'{"Choice":^10}' +\
          f'{"Description":20}' + \
          f'{"Qty":>5} ' + \
          f'{"Price":>15}')
    print(f'{"------":^10}' +\
          f'{"-----------":20}' + \
          f'{"---":>5}' + \
          f'{"-----":>15}')   
    for counter in range(len(ritems)):
        print(f'{counter + 1:^10} {ritems[counter]}')
    choice = int(input('Enter your choice (0 to check out): '))
    # validation of numeric input
    while (choice < 0 or choice > len(ritems)):
        print('ERROR! Invalid choice.')
        choice = int(input('Enter your choice (0 to check out): '))
    return choice

def checkOut(cReg):
    ''' display, total, and check out all items from cash register '''
    totalAmt = cReg.get_total()
    taxAmt = cReg.get_tax_amt()
    print('Shopping Cart')
    print('-------------')
    cReg.show_items()
    print(f'\n{"Subtotal":<15}${totalAmt:>15,.2f}')
    print(f'{"Tax":<15}${taxAmt:>15,.2f}')
    print(f'{"Tax Rate":<15} {cReg.TAX_RATE:>15.2%}')
    print(f'{"Total":<15}${totalAmt + taxAmt:>15,.2f}')
    print(f'\nCheck out complete.  Clearing cash register...')
    cReg.clear()
    if len(cReg.items) == 0:
        print('Cash register cleared.')
    

def main():
    ''' create inventory, process user menu selection within loop '''
    inventory = (r.RetailItem('Jacket', 12, 59.95),
                 r.RetailItem('Designer Jeans', 40, 34.95),
                 r.RetailItem('Shirt', 20, 24.95),
                 r.RetailItem('Breitling Top Time', 5, 19900.00))
    register = cr.CashRegister()
    uchoice = menuChoice(inventory)
    # loop while items to purchase
    while(uchoice != 0):
        qty = int(input('Quantity to purchase: '))
        # validation of numeric input
        while(qty < 1 or qty > inventory[uchoice - 1].units):
            print(f'ERROR! Invalid quantity.')
            print(f'Valid quantity is 1 to {inventory[uchoice - 1].units}.')
            qty = int(input('Quantity to purchase: '))
        # create item to purchase
        itemToPurch = r.RetailItem()
        itemToPurch.description = inventory[uchoice - 1].description
        itemToPurch.units = qty
        itemToPurch.price = inventory[uchoice - 1].price
        # add item to cash register
        register.purchase_item(itemToPurch)
        # update inventory quantity for additional purchase
        inventory[uchoice - 1].units -= itemToPurch.units
        # redisplay menu and get selection
        uchoice = menuChoice(inventory)
    # display items in cart
    print(f'Checking out....\n')
    checkOut(register)
    print(f'Thank you for visiting the COD Student Store today!\n')
   
    
if __name__ == '__main__':
    main()