"""
1) Take 2 numbers are find which one is greater than the other
2) Take the greater number and
"""


# Program Starts

def getgreatnumber():
    a = 1000000000000
    b = 1200000000000
    if b > a:
        print("b is greater than a")
        return b
    elif a == b:
        print("a and b are equal")
        return 0
    else:
        print("a is greater than b")
        return a

# Global Variables

name = "Chakra"


def cal():
    # local Variables
    """
     These are illegel variable name assignments
    2myvar = "John"
    my-var = "John"
    my var = "John"
    """
    # These are legel variable name assignments
    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"
    # snakecase
    my_variable_name = "John"
    # pascalcase
    MyVariableName = "John"
    # camelcase
    myVariableName = "John"
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)

     # To change the value of a global variable inside a function, use global keyword
    global name
    name = "john"
    print(name)
    print("The Fruit Name is " + x)


def printgreatnumber():
    print(getgreatnumber())
    cal()
