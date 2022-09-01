#ex15.py
#READING FILES

from sys import argv
script, filename = argv

txt = open(filename) #Opens the file
print(f"Here is your file {filename}:\n")
print(txt.read()) #Reads the file that was opened!

txt_again = open(filename)
print("Type the filename again: ") #Prompts the user
file_again = input('> ') #Awaits for user imput
print(txt_again.read()) #Reads the file that was opened!
