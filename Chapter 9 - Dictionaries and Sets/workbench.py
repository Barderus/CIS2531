'''
Workbench ch9
'''

# Displays the value of Tuesday
dct ={ "Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6, "Sunday":7}
print("Tuesday value: ", dct["Tuesday"])

# Display the value of Monday if it exists
print("Display the value of Monday: ", dct.get("Monday", "Not found"))

# Display not found if the key does not exist
print("Does Fryday exist: ",dct.get("Fryday", "Not found"))

# Delete an element from the dictionary
del dct["Friday"]
print("Does Friday exist: ",dct.get("Fryday", "Not found"))

# New dictionary
dct1 = {1:[0,1], 2:[2,3], 3:[4,5]}
# Displays [4,5]
print(dct1[3])
# Print the keys of the dct1 set
for k in dct1:
    print("Key:", k)

# Only adds to the set a, b, c, d, and empty space
myset = set("a bb ccc dddd")
print(myset)
# Only adds to the set 2,4,6
myset1 = set([2,4,4,6,6,6,6])
print(myset1)

# Write an if statement that determines whether the key "James" exists in the dictionary. If so,
# Display the value that is associated with that key. If the key is not in the dictionary,
# Display a message saying so
name = input("Enter user name: ")
dct2 = {"Gabriel":27, "Fiona":22, "Henry":10, "Davod":14, "James":21}
if dct2.get(name):
    print(dct2[name])
else:
    print("Not found")
    
dct3 = {"Gabriel":27, "Fiona":22, "Henry":10, "Davod":14, "James":21, "Jim":51}
if name in dct3:
    print(f"Deleting {name}...")
    del dct3[name]
    print(dct3)
else:
    print("Not found")
    

# Set comprehension
numbers = [1,2,3,4,5]
dctNum = {n:n*10 for n in numbers}
print(dctNum)

# High scores set comprehension
test_averages = {"Janelle":98, "Sam":87, "Jennifer":92, "Thomas":74, "Sally":89, "Zeb":84}
high_scores= {k:v for k,v in test_averages.items() if v >= 90}
print(high_scores)