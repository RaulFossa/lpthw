#ex14.py
#Prompting & Passing

from sys import argv

script, user_name = argv
prompt = '> '#variable

print(f"Hi {user_name}, I'm {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}? ")
likes = input(prompt)#prompts the user and store value

print(f"Where do you live {user_name}? ")
lives = input(prompt) #Value has changed

print(f"What kind of computer do you have? ")
computer = input(prompt) #Value has changed

#f"" f-string
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
\n""")
