#ex5.py
#F-STRINGS
#Format strings with {EMBEDED} variables
#Add an "f" before you initiate a string
#example: print(f"Hello world!")

my_name = "Zed A. Shaw"
my_age = 35
my_height = 74 #inches
my_weight = 180 #I wish
my_eyes = "blue"
my_teeth = "white"
my_hair = "brown"
#f"" before the string.
print(f"let's talk about {my_name}.")
print(f"{my_name} is {my_height} inches tall.")
print(f"He is {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He is got {my_eyes} eyes and {my_hair} hair.")
print(f"His theeth are usually {my_teeth} depending on the coffee.")

#This line of code is tricky, pay attention!
#New variable "total" will add variables
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}.")


#Added a space before the next code
#print(\n) new line
print("\n")

#Variables (strings and integers)
#Another way is to create a variable with .format() after the string
#Don't forget to print(variables)
name = "Raul"
last_name = "Fossa"
age = 42
#Using format() to use a var inside a str.
first = "Hello my name is {}".format(name)
print(first)
last = "My last name is {}".format(last_name)
print(last)
how_old = "I am {} year old!".format(age)
print(how_old)

print("\n") #new line

#Change pounds to kilograms
#float() receives int & float
lbs = float(input("How many lbs do you weight? ")) #float()
kg = lbs / 2.205 #lbs to Kgs formula
print(f"If we convert {lbs} lbs to kilograms, you are: ")
print(round(kg), "kilograms") #round() will round up a float.

#Change centimeters to inches
cent = float(input("How many centimeters? ")) #float()receives int & float
inch = cent * 2.54
print(f"{cent} centimeters is:")
print(round(inch), "inches") #round() will round up a float.


#NOTES
#f-strings have {embeded} Variables print(f "blah blah {variable} blah")
#New lines in the code "\n"
#round() function will round up when a float is returned.
