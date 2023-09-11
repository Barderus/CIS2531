'''
Author: Gabriel dos Reis
Date: 9 / 7 / 2023
Program: restaurantSelec
Description: Write a program that asks whether any members of your party are vegetarian,
vegan, or gluten-free, to which then displays only the restaurants to which you may take
the group. 

    * Joe's Gourmet Burguers
        Veg no, Vegan no, gluten free no
    * Main Street Pizza Company
        Veget yes, vegan no, gluten free yes
    * Corner Cafe
        Veget yes, vegan no, Gluten free yes
    * Mama's Fina Italian
        Veget yes, vegan no, gluten-free no
    * The Chef's Kitchen
        Veget yes, vegan yes, gluten-free yes

'''

vegetarianPeeps = input("Is anyone in your party vegetarian?: ")
vegetarianPeeps.lower()
veganPeeps = input("Is anyone in your party vegan?: ")
veganPeeps.lower()
glutenFreePeeps = input("Is anyone in your party gluten-free?: ")
glutenFreePeeps.lower()

if vegetarianPeeps == "yes" and veganPeeps == "yes" and glutenFreePeeps == "yes":
    print("Your restaurant choices is: The Chef's Kitchen")
elif vegetarianPeeps == "yes" and veganPeeps == "no" and glutenFreePeeps == "no":
    print("Your restaurant choices is: Mama's Fina Italian")
elif vegetarianPeeps == "yes" and veganPeeps == "no" and glutenFreePeeps == "yes":
    print("Your restaurant choices are: \n\t Corner Cafe \n\t Main Street Pizza Company \n\t The Chef's Kitchen")
else:
    print("Your restaurant choices are: \n\t Joe's Gourmet Burguer \n\t Main Street Pizza Company \n\t Corner Cafe \n\t Mama's Fina Italian \n\t The Chef's kitchen") 