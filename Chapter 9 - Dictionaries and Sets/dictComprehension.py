'''
Dictionary Comprehension
'''

list1  = [1,2,3,4]

# Creates a dictionary with the key 1,2,3,4 with the 1,4,9,16 values
dict1 = {n:n**2 for n in list1}

# Creates a dictionary equal to dict1
dict2 = {k:v for k,v in dict1.items()}

# Creates a dictinary with only values bigger than 5
dict3 = {k:v for k,v in dict1.items() if v > 5}

print("\n", dict1)

print("\n", dict2)

print("\n", dict3)

curr_prices = {"Milk" : 2.49, "coffee" : 4.99, "bread" : 3.29}
new_prices = {k:v*1.1 for k,v in curr_prices.items()}
print("\nNew prices: ", new_prices)

quiz_results = {"Kayla" : 5, "Larry" : 9, "Bob" : 6, "Sally" : 8}
quiz_retake = {k:v for k,v in quiz_results.items() if v < 7}
print("These students can retake the quiz: ", quiz_retake)