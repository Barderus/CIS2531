'''
Iterables intro
'''

one_tuple = (1,2,3)
tens_list = [10,20,30,40]

def average(*args):
    return sum(args) / len(args)

print(average(1,2))

print(average(1,2,3,4,5))

# Allow to get the values inside the tuple/list
print(average(*one_tuple))

print(average(*tens_list))

# Zip 
cards = ("Jack", "Queen", "King", "Ace")
values = (11, 12, 13, 1)

for c,v in zip(cards, values):
    print("{:>10} {:>5}".format(c,v))
    
# Enumerate, adds a counter to the object
eCards = enumerate(cards)
for c,v in eCards:
    print(c,v)
print()  
# Set a start counter for the enumerator
for c,v in enumerate(cards, start= 11):
    print(c,v)

print()  
# Map function
def strToUpper(string):
    return str(string).upper()
    
for each in map(strToUpper, cards):
    print(each)