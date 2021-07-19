from math import pi

def print_type(variable):
    """This function prints the type of supplied variable
    Args:
        variable (Any): variable to print type for
    """
    if isinstance(variable, bool):
        print("variable is boolian")
    elif isinstance(variable, float):
        print("variable is float")
    elif isinstance(variable, int):
        print("variable is int")
    elif isinstance(variable, list):
        print("variable is list")

def do_action(variable):
    """Does the action depending on variable's type. (hint: you can either use print function right here,
    or return the result. For now it doesn't matter)
    Defined actions:
        int: square the number
        float: and ПЂ(pi) (from math.pi, don't forget the import~!) to it and print the result
        bool: inverse it (e.g if you have True, make it False) and print the result
        list: print elements in reversed order
    Args:
        variable (Any): variable to perform action on
    """
    if isinstance(variable, bool):
        print("reversed boolian is", not(variable))
    elif isinstance(variable, float):
        print("float*pi is", variable*pi)
    elif isinstance(variable, int):
        print("sqare of the int is", variable*variable)
    elif isinstance(variable, list):
        print("reversed list is", variable[::-1] )

variables = [ 42, 45.0, True, False, [16, 9, 43, 65, 97, 0]]

for element in variables:
    # Please, for all elements in `variables` list print the following:
    #  the type of variable using `print_type` function
    #  and the action for variable using `do_action` function
    print_type(element)
    do_action(element)
