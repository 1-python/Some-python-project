import random
import time
username = input("What's your username ?")
words = []

while True:
    try:
        number_words = int(input("How many words ?"))
        break
    except(ValueError):
        print("Please enter a valid number...")
       

for w in range(number_words):
    word = input(f"Give me one word {username}... ({w+1}/{number_words})")
    words.append(word)

guess = random.choice(words)

user_input = (input("Guess my word !"))

if user_input == guess:
        print("You won !")
        time.sleep(2)
else:
        print(f"No :( ! It was {guess}.")
        time.sleep(2)
    


    





