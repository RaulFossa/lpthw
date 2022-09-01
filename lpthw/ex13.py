#ex13.py
#Parameters, Unpacking, Variables.

from sys import argv #argv (Argument variable)
#import. This is how to add features from the python fautures set (library)
#Libraries or modules
#read the WYSS section for how to run this

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)



age = input("age? ")
print("Your age is", age)

#OR

print("age?", end = ' ')
age = input()
print(age)


#ATTENTION! PLEASE REVISIT
#argv #gives input (parameters) in the command line
#input() #givesinput on the keyboard when the script is running
