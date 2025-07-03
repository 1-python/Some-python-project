name = input("What's your name ?")
date = input("What's the date today ?")
day = input("How was your day ? Can you say what have you done today ?")

with open(f"journalof{name}.txt", "a")as file:
    file.write(f"\n{date}\n{day}")