'''
Author:
Date:
Prorgram:
Description:
'''

def greeting(name="everybody"):
    ''' Function to greet someone.'''
    print("Hello", name)

def main():
    print("greeting functio docstring:", greeting.__doc__)
    greeting("Gabriel")
    greeting()
