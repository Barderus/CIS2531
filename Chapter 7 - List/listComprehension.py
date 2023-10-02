'''
List comprehension
'''
list1 = [1,2,3,4,5,6,7,8]
list2 = [n for n in list1]
list3 = [n**2 for n in list1]
list4 = [n for n in list1 if n > 5]

print("List1: ", list1)
print("List2: ", list2)
print("List3: ", list3)
print("List4 ", list4)

# Examples
nums1to10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print numbers 1 to 5
nums1to5 = [n for n in nums1to10 if n <= 5]
print(nums1to5)
# Print numbers 5 to 10
nums5to10 = [n for n in nums1to10 if n >= 5]
print(nums5to10)
# print even numbers
evenNumbers = [n for n in nums1to10 if n % 2 == 0]
print(evenNumbers)
# Print oddN umbers
oddNumbers = [n for n in nums1to10 if n % 2 > 0]
print(oddNumbers)

# Get a list with only CIS1400
pythonClasses = ["CIS1400", "CIS2531", "CIS232"]
introPython = [n for n in pythonClasses if "CIS1" in n]
# OR
introPython2 = []
for n in pythonClasses:
    if "CIS1" in n:
        introPython2.append(n)

print(introPython2, introPython)

# Get a list with CIS2531, CIS2532
advPython = [n for n in pythonClasses if "CIS2" in n]
# OR
advPython2 = []
for n in pythonClasses:
    if "CIS2" in n:
        advPython2.append(n)
        
print(advPython)
print(advPython2)