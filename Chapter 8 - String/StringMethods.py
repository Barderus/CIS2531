'''
Strings methods
'''
greeting = "Hello World"
# Count the amount of that in a sequence 
greeting.count("L")

greeting.isupper()

greeting.islower()

greeting.isdigit()

tired = "z"
sleepinig = tired * 10
print(sleepinig)

today = "10/9/2023"
dateList = today.split("/")
print(dateList)

for n in dateList:
    print(n)
    
'''
center(width) to center the string
ljust(width) to left justify to a certain width
rjust(width) to right justify to a certain width
'''