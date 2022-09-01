#ex7.py
#More printing in order to find mistakes
#Variables missing, etc... Go!
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
#Inside the format() there is no variable
#If using a string .format('string'), there is no need to declare a var
print("And everywhere that Mery went.")
print("." * 10) #Prints ..........

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#Watch end = ' ' at the end
#Try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') #,end=' '
print(end7 + end8 + end9 + end10 + end11 + end12)
#,end= ' ' will print all in one (1) line
#Like this "Cheese Burger"
#NOT like this Cheese
#              Burger
