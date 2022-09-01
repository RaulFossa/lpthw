#ex19.py
#More FUNCTIONS & Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#Variables
cheese_and_crackers(20, 30)

#..........................
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#..........................
cheese_and_crackers(10 + 20, 10 + 20)

#User input and passing them into a function as arguments

def nuts (chia, almonds, cashews):
    print("You have:")
    print(f"\t>{chia} Chia seeds")
    print(f"\t>{almonds} Almonds")
    print(f"\t>{cashews} Cashews\n")

prompt = '>'

print("Number of Chia Seeds? ", end = '')
chia_num = int(input(prompt))
print("Number of Almonds? ", end = '')
almonds_num = int(input(prompt))
print("Number of Cashews? ", end = '')
cashews_num = int(input(prompt))

nuts(chia_num, almonds_num, cashews_num)

total_nuts = chia_num + almonds_num + cashews_num
print(f"You have a total of {total_nuts} nuts :)")
