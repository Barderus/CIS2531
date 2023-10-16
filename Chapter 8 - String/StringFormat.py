'''
String formatting
'''

myClass = "Python Programming"
numCredits = "4"

#print("%s is %.1f credit hours" % (myClass, numCredits))

#print(format(myClass, "s") + " is " + format(numCredits, ".1f") + "credit hurs.")

#print(f"{myClass:s} is {numCredits:.1f} credit hours")

#print("{1} is {0:.1f} credit hours".format(numCredits, myClass))

myString = "Hello World"
myInt = 12345
myFloat = 12345.6789

print('{} \n {} \n {}'.format(myString, myInt, myFloat))
print()
print('{:30s} \n{:30d} \n{:30.3f}'.format(myString, myInt, myFloat))
print()
print('{:>30s} \n{:>30d} \n{:>30.3f}'.format(myString, myInt, myFloat))
print()
print('{:<30s} \n{:<30d} \n{:<30.3f}'.format(myString, myInt, myFloat))
print()
print('{:^30s} \n{:^30d} \n{:^30.3f}'.format(myString, myInt, myFloat))
print()
print('{:^30s} \n{:^30,d} \n{:^30,.3f}'.format(myString, myInt, myFloat))
print()

print(format(23.456, "30,.2%"))

'''
            # Display     Display DJIA closing price averages for YYYY
            #               Month           Average
            #               =====           =======
            print(f"{message}{year}\n{monthMsg:>30}\t{avgMsg:>30}\n{delimiterMsg:>30}\t{delimiterMsg:>30}")
'''