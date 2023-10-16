'''
Set comprehension
'''

set1 = {1,2,3,4,5,6,7,8}

set2 = {n for n in set1}

set3 = {n**2 for n in set1}

set4 = {n for n in set if n > 5}

even_less10 = {2,4,6,8,10}
num1To5 = {1,2,3,4,5}
num1To10 = {1,2,3,4,5,6,7,8,9,10}

evenNumbers = {n for n in even_less10}

evenNumbers = {n * 2 for n in num1To5}

evenNumbers = {n * 2 for n in range(1,6)}

evenNumbers = {n for n in num1To10 if n % 2 == 0}

evenNumbers = {n for n in range(1,11) if n % 2 == 0}

