'''
Given decimal and base, convert decimal number to base
Then, display the converted number.
'''

def conv_to_base(n, b):
    if n > 0:
        conv_to_base(n//b, b)
        print(format(n%b, "X"), end='')
conv_to_base(13, 16)