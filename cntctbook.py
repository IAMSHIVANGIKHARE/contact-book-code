# Contact Book Program

# Function to add a contact
def add_contact(contact_book):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact_book[name] = {"phone": phone, "email": email}
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contact_book):
    if not contact_book:
        print("No contacts found.")
        return
    for name, details in contact_book.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("-" * 20)

# Function to search for a contact
def search_contact(contact_book):
    name = input("Enter contact name to search: ")
    if name in contact_book:
        details = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print("Contact not found.")

# Main program
def main():
    contact_book = {}
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contacts(contact_book)
        elif choice == '3':
            search_contact(contact_book)
        elif choice == '4':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main program
if __name__ == "__main__":
    main()
