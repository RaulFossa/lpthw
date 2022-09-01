#ex16.py
#READING & WRITING FILES

from sys import argv
script, filename = argv #Add files name on comand line

print(f"We're going to erase {filename}.") #f string
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?") #Waits for user

print("Opening the file...")
target = open(filename, 'w') #Opens the file 'w' to write

print("Truncating the file. Goodbye!")
target.truncate() #truncate (deletes)

print("Now I'm going to ask you three lines.")

#Prompts the user for 3 lines and stores them in each Var
line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("I'm going to write these to the file.")

#Writes the lines into the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"This is the file {filename} you created:")#f string
#Read file created
target = open(filename) #Open file
print(target.read()) #Reads the file to the screen

print("And finally,we close it.")
target.close() #Closes the file with close() function/method
