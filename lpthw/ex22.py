#ex22.py
#PRACTICE CONCEPTS
#What Do You Know So Far?

#DOCSTRING COMMEMT USING """ QUOTES.

"""
*** SYMBOLS & CHARACTERS ***

*Quotes ('',"", """ """) Single, Double, Triple
*Python data (Strings, Integers, Booleans (True/False))
*Integers (Whole numbers)
*Floats (Decimal numbers ex. 30.0)
*BOOLEANS = True or False

* MATHEMATICAL SYMBOLS

(*) Multiplication
(/) Division
(+) Adition
(-) Subtraction
(**) Exponent (2**3) = (2*2*2)
(%)  Modulus (The reminder!) 9 % 2 = 1
(//) Floor Division 10 // 3 = 3

* PYTHON ASSIGNMENT OPERATORS

(=)	 x = 5     same as x = 5
(+=) x += 3	   same as x = x + 3
(-=) x -= 3	   same as x = x - 3
(*=) x *= 3	   same as x = x * 3
(/=) x /= 3	   same as x = x / 3
(%=) x %= 3	   same as x = x % 3
(//=) x //= 3  same as x = x // 3
(**=) x **= 3  same as x = x ** 3
(&=)  x &= 3   same as x = x & 3

(|=)  x |= 3   same as x = x | 3
>>> A = True
>>> B = False
>>> B |= A
>>> B
True

(^=)  x ^= 3   same as x = x ^ 3
(>>=) x >>= 3  same as x = x >> 3
(<<=) x <<= 3  same as x = x << 3

*STRINGS FORMATTING

\n = New line
\t = tabbed (4 spaces)
end = ' ' (Same line)
(f"") F-strings (Adds a var into a string, print(f"Hello {world}"))
\ = Skips character inside a string. print('Hello I\'m MacOs.')

*USER PROMPTS

age = input("age? ")
print("Your age is", age)
#OR
print("age?", end = ' ')
age = input()
print(age)

*FUNCTIONS OR METHODS

truncate()
new_file = open(input_file, 'w')
new_file.truncate()

print("Hello World!")

read()
new_file = open(input_file)
print(new_file.read())

readline()
#The readline() method returns one line from the file
f = open("demofile.txt", "r")
print(f.readline())

#You can also specified how many bytes from the line to return,
by using the size parameter.
file.readline(size)

#Return only the five first bytes from the first line:
f = open("demofile.txt", "r")
print(f.readline(5))

write()
new_file.write(line1)
new_file.write('\n')

format()
sport = "skateboarding"
print("I love {}".format(sport))
output - I love skateboarding

input()
print("Line 1: ")
line1 = input()

open()
new_file = open(input_file)

close()
out_file.close()
first_file.close()
second_file.close()

exists()
#Use from os.path import exists
#Returns a Boolean True or False.
exists(file)

seek()
#seek() method sets the current file position in a file stream.
#seek() also returns the new postion.

Change the current file position to 4, and return the rest of the line:
f = open("demofile.txt", "r")
f.seek(4)
print(f.readline())

*HOW TO FUNCTION

*EXAMPLE CODE*
def fruits (apples, bananas):
    print(f"You have {apples_num} apples.")
    print(f"You have {bananas_num} bananas.")
    return apples + bananas

prompt = '>'

print("How many apples? ")
apples_num = int(input(prompt))

print("How many bananas? ")
bananas_num = int(input(prompt))

total = fruits(apples_num, bananas_num)

print(f"You have a total of {total} fruits.")

*OUTPUT*
raul_andres $python3 ex22.py
How many apples?
>13
How many bananas?
>7
You have 13 apples.
You have 7 bananas.
You have a total of 20 fruits.
raul_andres $
----------------------------------------------

Create a function checklist for later exercises. Write these checks
on an index card and keep it by you while you complete the rest of
these exercises or until you feel you do not need the index card anymore:

1. Did you start your function definition with def?
2. Does your function name have only characters and _ (underscore)
characters?
3. Did you put an open parenthesis right after the function name?
4. Did you put your arguments after the parenthesis separated by commas?
5. Did you make each argument unique (meaning no duplicated names)?
6. Did you put a close parenthesis and a colon after the arguments?
7. Did you indent all lines of code you want in the function four
spaces? No more, no less.
8. Did you “end” your function by going back to writing with no
indent (dedenting, we call it)?

When you RUN (“USE” or “CALL”) a function, check these things:

1. Did you call/use/run this function by typing its name?
2. Did you put the ( character after the name to run it?
3. Did you put the values you want into the parentheses
separated by commas?
4. Did you end the function call with a ) character?

Use these two checklists on the remaining lessons until you do not
need them anymore. Finally, repeat this a few times to yourself:
To “RUN,” “CALL,” or “USE” a function each means the same thing.
"""
