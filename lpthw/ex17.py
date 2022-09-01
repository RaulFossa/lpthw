#ex17.py
#Doing MORE with Files.

#***COMAND LINE***
#echo "This is a new file" > Test.txt (Creates a new file from CL)
#cat "Reads" the file created

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

#exists() returns True if a file exists, based on its NAME
#in a string as an argument. It returns False if not.
print(f"Does the output file exist? {exists(to_file)}") #Returns Boo
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') #Creates a NewFile
out_file.write(indata)

print("Alright, all done.")

out_file = open(to_file) #opens new file
print(out_file.read()) #Reads new file

#Closes the file with close() function/method
out_file.close()
in_file.close()
