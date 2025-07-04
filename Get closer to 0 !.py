import random
import time
number_players = int(input("How many players? "))

scorelist = []

for w in range(number_players):
    username = input("Give us your username... ").capitalize()
    print(f"Welcome, {username}!")
    
    secret_number = random.randint(-1000, 1000) # random number to compare
    print("Your goal is to be as close to zero as possible, without knowing the number.")
    print("It could be from -1000 to 1000!")
    
    number_count = int(input("How many numbers will you use? "))
    number_list = []
    number_list.append(secret_number)

    for i in range(number_count):
        val = int(input("Number... "))
        number_list.append(val)

    operation = input("Type '+' to add all numbers...")

    # Calculate result
    if operation == "+":
        result = sum(number_list)
    else:
        print("Error, we don't support any other operation other that additions")

    print(f"Total: {result}")
    
    # Compare to 0
    if result == 0:
        print("🎉 You are the best, you got 0!")
    elif result > 0:
        print(f"The base number was {secret_number}! You have {result}!")
    else:
        print(f"The base number was {secret_number}! You got {result}!")
        
    # Calculate how close result is to zero (distance)
    distance = abs(result)
    scorelist.append((username, distance))

# Write scores to file
with open("score.txt", "a") as file:
    for name, dist in scorelist:
        file.write(f"{name} : {dist}\n")

print("Scores:")
for name, dist in scorelist:
    print(f"{name} was {dist} away from zero.")
    time.sleep(5)
