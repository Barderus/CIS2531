'''
Set Analysis
'''
cis1400set = {"Joseph", "Jessica", "Rueben", "Gabriel"}

cis2531set = set(["Gabriel", "Marinana", "Fiona"])

# Union of both sets
print(cis1400set | cis2531set)

# Intersection
# Or cis1400set.intersection(cis2531set)
print(cis1400set & cis2531set)

# Difference
print(cis1400set - cis2531set)

# Symmetric difference
print(cis1400set ^ cis2531set)