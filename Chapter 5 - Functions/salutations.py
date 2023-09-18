'''
Author:
Date:
Prorgram:
Description:
'''

def salutations(*names):
    ''' Function to greet everyone in a list. '''
    for one_name in names:
        print("Hello,", one_name)

def main():
    print("Salutation function docstring:")
    salutations("Gabriel", "Henry", "David")
    # Does not display anything
    salutations()
    salutations("Fiona")
    
main()