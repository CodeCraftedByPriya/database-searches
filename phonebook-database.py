# Phone book
pb = {}

def add(name, phone_number):
    pb[name] = phone_number

def search(name):
    if name in pb:
        print(f"{name}'s phone number is {pb[name]}")
    else:
        print(f"{name} not found in phonebook")

def delete(name):
    if name in pb:
        del pb[name]
    else:
        print(f"{name} not found in phonebook")

def show():
    if not pb:
        print("Phonebook is empty")
    else:
        print("Phonebook:")
        for name, phone_number in pb.items():
            print(f"{name}: {phone_number}")

print("1. Add contact")
print("2. Search contact")
print("3. Delete contact")
print("4. Print all contacts")
print("5. Exit")
            
while True:
    print("")
    c = int(input("Enter option: "))
    print("")
    if c == 1:
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        add(name, phone_number)
    elif c == 2:
        name = input("Enter name to search: ")
        search(name)
    elif c == 3:
        name = input("Enter name to delete: ")
        delete(name)
    elif c == 4:
        show()
    elif c == 5:
        break
    else:
        print("Invalid option, please try again")
