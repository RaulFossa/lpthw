#ex11.py
#Asking Questions!
#Using input() function
#end = ' ' This tells print() not to end the line with a newline...
#wih a character and fgo to the next line

print("How old are you? ", end = ' ')
age = input()
print("How tall are you? ", end = ' ')
height = input()
print("How much do you weight? ", end = ' ')
weight = input()

print(f"So you are {age} old, {height} tall and {weight}lbs heavy.\n")

#Another way is to input() & store the return in a variable
#Use int(), float() if expecting a number
new_age = int(input("How old are you? "))
print(f"Your are {new_age} years old! ")
