#ex18.py
#FUNCTIONS

def print_two(*args): #Not used very often
    arg1, arg2 = args #Very similar than "argv"
    print(f"arg1: {arg1}, arg2: {arg2}")

#.......................................

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin!")

#variables
print_two("Raul", "Fossa")
print_two_again("Raul", "Fossa")
print_one("First!")
print_none()
