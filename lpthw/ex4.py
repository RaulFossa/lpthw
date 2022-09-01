#ex4.py
#Variables & Names
#Variables declared with values!
#Some variables can add mathematical values
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

#After all variables are declared
#print functions will get the chance to use them.

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put", average_passenger_per_car, "in each car.")
#We have used all var while printing str.
