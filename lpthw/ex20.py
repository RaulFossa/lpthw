#ex20.py
#FUNCTIONS & FILES

from sys import argv

script, input_file = argv

def print_all (f):
    print(f.read())

def rewind (f):
    f.seek(0) #Moves to start of the file

def print_a_line (line_count, f):
    print(line_count, f.readline())

current_file = open(input_file) #Opens the input_file
print("Printing input file...\n")
print_all(current_file) #Passing the argument to print_all func. (f)

print("Rewinding input file...\n")
rewind(current_file)#Passing the argument to rewind() func. (f)

print("Printing 3 lines from  input file\n")

current_line = 1
print_a_line(current_line, current_file)
#Arguments to print_a_line func. (line_count, f)

current_line += 1 #OR current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
