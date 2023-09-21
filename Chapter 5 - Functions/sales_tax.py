'''
Sales Tax
'''

STATE_TAX = 0.05
COUNTY_TAX = 0.02


def get_state_tax(money):
    state_tax = money * STATE_TAX
    return state_tax
    
def get_county_tax(money):
    county_tax = money * COUNTY_TAX
    return county_tax
    
def get_total(state_tax, county_tax, money):
    ttl = state_tax + county_tax + money
    return ttl
    
    
def main():
    purchase = float(input("Enter the amount of the purchase: "))
    state_tax = get_state_tax(purchase)
    county_tax = get_county_tax(purchase)
    ttl_pay = get_total(state_tax, county_tax, purchase )
    print("State tax: $", state_tax," \nCounty Tax: $", county_tax, "\nPurchase amount: $", purchase, "\nTotal to pay: $", ttl_pay )

main()