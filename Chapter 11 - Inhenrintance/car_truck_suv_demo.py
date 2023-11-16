'''
This program will create a Car object, a Truck object,
and a SUV object to use polymorphism to determine
the off road capability
'''
import Automobile as a

def display_offRoad_cap(auto):
    '''
    This function to display off road capability
    that will invoke the appropriate implementation
    of the is_off_road method based upon the passed
    object
    '''
    if isinstance(auto, a.Automobile):
        if auto.is_off_road():
            print("--> This vehicle is an off road vehicle.")
        else:
            print("--> This vehicle is NOT an off road vehicle")
    else:
        print("--> This vehicle is NOT an automobile.")
    print()
    return

def main():
    car = a.Car("BMW", "330i", 70000, 1500.0, 4)
    truck = a.Truck("Toyota", "Tacoma", 40000, 12000.0, "4WD")
    suv = a.SUV("Volvo", "XC40", 30000, 18500.0, 5)
    
    print("USED CAR INVENTORY")
    print("===================")
    print(car)
    display_offRoad_cap(car)
    
    print(truck)
    display_offRoad_cap(truck)
    
    print(suv)
    display_offRoad_cap(suv)
    
    print("Testing")
    display_offRoad_cap("testing")
    
main()