# Day 2 - Contact Book Application

## 📌 Project Overview

As part of my 100 Days, 100 Project Ideas journey, I built a command-line Contact Book application using Python and Object-Oriented Programming.

The application allows users to add, view, search, and delete contacts. Contact information is stored in a JSON file so that the data remains available after restarting the application.

## 🚀 Features

- Add contacts
- View all contacts
- Search contacts by name
- Delete contacts
- Validate name, phone number, and email
- Save contacts to JSON
- Load contacts automatically when the application starts
- Handle invalid user input

## 🛠️ Technologies

- Python
- Object-Oriented Programming
- JSON
- File Handling
- Exception Handling

## 🧠 Concepts Practiced

- Classes
- Objects
- `__init__()`
- `self`
- Attributes
- Methods
- Lists of objects
- Loops
- Conditional statements
- Input validation
- Exception handling
- JSON serialization and deserialization

## 📂 Project Structure

```text
day02-contact-book/
│
├── contact_book.py
├── contacts.json
└── README.md

▶️ How to Run
python contact_book.py

📋 Application Menu
===== CONTACT BOOK =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit
💾 Data Persistence

Contacts are stored in contacts.json.

Example:

[
    {
        "name": "Lakshana",
        "phone": "9876543210",
        "email": "lakshana@gmail.com"
    }
]

The application loads this data when it starts and saves changes whenever contacts are added or deleted.

🎯 What I Learned

This project helped me understand how Object-Oriented Programming can organize a real application.

I learned how to:

Create classes and objects
Store objects inside lists
Create methods for different operations
Validate user input
Convert objects into JSON-compatible data
Load saved data back into Python objects
Structure a menu-driven CLI application


🔮 Future Improvements
Edit existing contacts
Add contact categories
Add phone-number validation using country codes
Add sorting and filtering
Add SQLite database support
Build a GUI/web version