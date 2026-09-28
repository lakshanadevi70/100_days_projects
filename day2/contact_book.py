import json


class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self.contacts = []

    # -------------------------
    # Add Contact
    # -------------------------
    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully!")

    # -------------------------
    # View Contacts
    # -------------------------
    def view_contacts(self):

        if len(self.contacts) == 0:
            print("No contacts found.")
            return

        print("\n===== CONTACTS =====")

        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name}")
            print(f"   Phone: {contact.phone}")
            print(f"   Email: {contact.email}")

    # -------------------------
    # Search Contact
    # -------------------------
    def search_contact(self):

        search_name = input("Enter name to search: ")

        found = False

        for contact in self.contacts:

            if search_name.lower() in contact.name.lower():

                print("\n===== CONTACT FOUND =====")
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")

                found = True

        if not found:
            print("Contact not found.")

    # -------------------------
    # Delete Contact
    # -------------------------
    def delete_contact(self):

        if len(self.contacts) == 0:
            print("No contacts available.")
            return

        self.view_contacts()

        try:

            contact_number = int(
                input("Enter contact number to delete: ")
            )

            if 1 <= contact_number <= len(self.contacts):

                deleted_contact = self.contacts.pop(
                    contact_number - 1
                )

                self.save_contacts()

                print(
                    f"{deleted_contact.name} "
                    "deleted successfully!"
                )

            else:
                print("Invalid contact number.")

        except ValueError:
            print("Please enter a valid number.")

    # -------------------------
    # Validate Name
    # -------------------------
    def validate_name(self, name):

        if name.strip() == "":
            return False

        return True

    # -------------------------
    # Validate Phone
    # -------------------------
    def validate_phone(self, phone):

        return phone.isdigit() and len(phone) == 10

    # -------------------------
    # Validate Email
    # -------------------------
    def validate_email(self, email):

        return "@" in email and "." in email

    # -------------------------
    # Save Contacts
    # -------------------------
    def save_contacts(self):

        data = []

        for contact in self.contacts:

            data.append({
                "name": contact.name,
                "phone": contact.phone,
                "email": contact.email
            })

        with open("contacts.json", "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # -------------------------
    # Load Contacts
    # -------------------------
    def load_contacts(self):

        try:

            with open("contacts.json", "r") as file:

                data = json.load(file)

            for item in data:

                contact = Contact(
                    item["name"],
                    item["phone"],
                    item["email"]
                )

                self.contacts.append(contact)

        except (FileNotFoundError, json.JSONDecodeError):

            pass


# ==================================
# MAIN PROGRAM
# ==================================

book = ContactBook()

# Load previously saved contacts
book.load_contacts()


while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # -------------------------
    # Add
    # -------------------------
    if choice == "1":

        name = input("Enter name: ")

        if not book.validate_name(name):

            print("Name cannot be empty.")
            continue

        phone = input("Enter phone: ")

        if not book.validate_phone(phone):

            print("Phone must contain exactly 10 digits.")
            continue

        email = input("Enter email: ")

        if not book.validate_email(email):

            print("Please enter a valid email.")
            continue

        contact = Contact(
            name,
            phone,
            email
        )

        book.add_contact(contact)

    # -------------------------
    # View
    # -------------------------
    elif choice == "2":

        book.view_contacts()

    # -------------------------
    # Search
    # -------------------------
    elif choice == "3":

        book.search_contact()

    # -------------------------
    # Delete
    # -------------------------
    elif choice == "4":

        book.delete_contact()

    # -------------------------
    # Exit
    # -------------------------
    elif choice == "5":

        print("Goodbye! 👋")
        break

    else:

        print("Invalid choice. Please enter 1-5.")