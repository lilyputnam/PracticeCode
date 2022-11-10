#This is a program that allows you to store your passwords

master_password = input("What is the master password? ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())
            user, passw = data.split("|")
            print("User:", user, ", Password:", passw)

#created a passwords.txt to keep track

def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + password + "\n")

while True:
    choice = input("Would you like to add a new password or view existing ones (view, add), press q to quit ").lower()
    if choice == "q":
        break
#using loops

    elif choice == "view":
        view()
    elif choice == "add":
        add()
    else:
        print("Invalid choice.")
