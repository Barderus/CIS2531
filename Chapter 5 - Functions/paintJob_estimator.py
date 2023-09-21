'''
Paint Job Estimator
112 ft of wall space = 1 gallon of paint, 8 hr of job, $35 p/h
Print: Number of gallons, hours required, cost of the paint, labor charges, ttl
Prompt user: wall space, price of paint p/ gallon
'''
import math

WALL_PAINT = 112
GALLON = 1
HOUR_JOB = 8
PRICE_PER_HOUR = 35

def paint_estimator(space, price):
    
    print("\t----------------")
    # Find how many gallons will be required and the price
    gallons = math.ceil( space / WALL_PAINT)
    print("\tYou will need", gallons, "gallons of paint")
    
    # Find how many hours will be required
    hours = math.ceil(space  / 14)
    print("\tWe will need", hours, "hours to complete this job")
    
    # Find the cost of labor
    cost = PRICE_PER_HOUR * hours
    print("\tThe cost of this labor is $", cost)
    
    # Calculate total 
    ttl = (gallons * price) + cost
    print("\tThe job will cost you $", ttl)
    print("\t------------------")
    
def main():
    wall_space = float(input("Enter how many feet of wall is going to be painted: "))
    gallon_price = float(input("Enter the price of the gallon of the paint: "))
    print()
    paint_estimator(wall_space, gallon_price)

    

main()