contacts = {}
while True:
    choice = input("Add [a] contact, view [v] all, or quit [q]...")

    if choice == "a":
        name = input("Name...")
        email = input("Email...")
        phone = input("Phone...")
        contacts[name] = {"email": email, "phone": phone}
    elif choice == "v":
        for name, info in contacts.items():
            print(f"{name} info : Email: {email}, Phone: {phone}")
    elif choice == "q":
        break

