'''
Intro to dictionary
'''

classDict = {"CIS1400" : "Programming",
             "CIS2531" : "Intro to Python Prog"}
print(classDict)

classDict["CIS1400"] = "Prog Logic & Tech"
print(classDict)

# Add CIS2532 key to the dictionary
classDict["CIS2532"] = "Adv Python Prog"
print(classDict)

# Checking if a key exist in the dictionary
print("Is CIS1400 in classDict?: ", "CIS1400" in classDict)
print("Is CIS1450 in classDict?: ", "CIS1450" in classDict)
print("Is CIS1400 not in classDict?: ", "CIS1400" not in classDict)

# Iterate the classDict and print the keys
for k in classDict:
    print(k, end=" ")


# Print the values of each key
for values in classDict.values():
    print(values)
    
# Print both the key and values together
for key, value in classDict.items():
    print(key, value)


'''
Practing Dictionary Methods
'''

# Delete the key CIS1400
print("\nDeleting CIS1400...")    
del classDict["CIS1400"]
for k, v in classDict.items():
    print(k,v)
    
# Look for CIS1400, if not found, prints "Not found"
classDict.get("CIS1400", "NOT FOUND")
classDict.get("CIS2531, NOT FOUND")

print(classDict.items())

classDict["CIS1400"] = "Prog Logic & Tech"

testKey = classDict.keys()
print("Dictionary keys = ", testKey)

testValue = classDict.values()
print("\nTesting values", testValue)

print("\nPopping 1450...")
print(classDict.pop("CIS1450", "NOT FOUND"))
k, v = classDict.popitem()
print(k,v)

# Clear method
classDict.clear()