'''
Sets
'''

# Ways to create set
cis1400set = {"Joseph", "Jessica", "Rueben", "Gabriel"}

cis2531set = set(["Mike", "Lynn", "Fiona"])

cis1450set = set()
cis1450set.update(["Gabriel", "Leonardo", "Miguel"])

for item in cis1450set:
    print(item, end=" ")
    
print(len(cis2531set))

# Adding elements to a set
cis1400set.add("Emily")
cis1400set.add("Matt")
print(cis1400set)

# Remove element of a set
cis1400set.remove("Emily")
print(cis1400set)

# Discard method to remove an element of a set
cis2531set.discard("Mike")

# Pop to remove an element of the set
el = cis1450set.pop()
print(el)

# Check if an item exists in a set

print("Matt" in cis1400set) 