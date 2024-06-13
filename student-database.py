# Student database
d = {}

def add(r, n, g, s):
    d[r] = {"name": n, "grade": g, "section": s}

def update(r, n=None, g=None, s=None):
    if r in d:
        if n:
            d[r]["name"] = n
        if g:
            d[r]["grade"] = g
        if s:
            d[r]["section"] = s
    else:
        print("Roll number not found!")

def delete(r):
    if r in d:
        del d[r]
    else:
        print("Roll number not found!")

def show():
    if not d:
        print("No students in the database!")
    else:
        print("Roll Number\t\t\t\tName\t\t\t\tGrade\t\t\t\tSection")
        for r, details in d.items():
            print(r, "\t\t\t\t", details["name"], "\t\t\t\t", details["grade"], "\t\t\t\t", details["section"])


print("\n")
print("\t\t1. Add student details")
print("\t\t2. Update student details")
print("\t\t3. Delete student details")
print("\t\t4. Display students details")
print("\t\t5. Exit the code")
print("\n")

while True:
    print("")
    c = int(input("Enter your task number: "))
    print("")
    if c == 1:
        r = int(input("Enter the roll number of the student: "))
        n = input("Enter the name of the student: ")
        g = int(input("Enter the class of the student: "))
        s = input("Enter the section of the student: ")
        add(r, n, g, s)
    elif c == 2:
        r = int(input("Enter the roll number of the student: "))
        n = input("Enter the updated name of the student: ")
        g = int(input("Enter the updated class of the student: "))
        s = input("Enter the updated section of the student: ")
        update(r, n, g, s)
    elif c == 3:
        r = int(input("Enter the roll number of the student: "))
        delete(r)
    elif c == 4:
        show()
    elif c == 5:
        break
    else:
        print("Invalid choice! Please enter a valid choice.")
