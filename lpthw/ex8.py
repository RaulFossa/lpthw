#ex8.py
#COMPLEX string formating
#.format() funtion just go real!
#Functiones tell python to do something

formatter = "{} {} {} {}"
#Using .format() you can place anything inside this {} {} {} {}
#4 slots will only store 4 values
print(formatter.format(1,2,3,4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True)) #Booleans too!
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
    " L\n",
    "U\n",
    "N\n",
    "A"
))
    #Strings over multiple lines. Sick!
    #"\n" New line
quit()
