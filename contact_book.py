import os

FILENAME = "contacts.txt"

# Load contacts from file
def load_contacts():
    contacts = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name},{phone}\n")

def show_menu():
    print("\n---- Contact Book ----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contacts[name] = phone
            save_contacts(contacts)
            print("Contact added!")

        elif choice == "2":
            if contacts:
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
            else:
                print("No contacts yet.")

        elif choice == "3":
            name = input("Enter name to search: ")
            if name in contacts:
                print(f"{name}'s number: {contacts[name]}")
            else:
                print("Contact not found.")

        elif choice == "4":
            name = input("Enter name to delete: ")
            if name in contacts:
                del contacts[name]
                save_contacts(contacts)
                print("Contact deleted.")
            else:
                print("Contact not found.")

        elif choice == "5":
            save_contacts(contacts)
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
