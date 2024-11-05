from add_contact import contacts
import re

def edit_contact():
    # Prompt the user to enter the phone number of the contact to edit
    phone_number = input("Please enter the phone number of the contact to edit (format 111-222-3333): ")

    # Check if the contact exists
    if phone_number not in contacts:
        print("Contact not found.")
        return
    
    # Display options for fields to edit
    print("""
            What would you like to edit:
            1. Name
            2. Phone Number
            3. Email Address
            4. Address
            5. Notes
    """)
    
    # Prompt the user to select an option to edit
    edit = input("Please choose an option to edit: ")
    
    # Edit the selected field
    if edit == "1":
        new_name = input("Enter the new name: ")
        contacts[phone_number]['name'] = new_name
        print("Name updated successfully.")

    elif edit == "2":
        while True:
            new_phone = input("Enter the new phone number (format 111-222-3333): ")
            if re.match(r'^\d{3}-\d{3}-\d{4}$', new_phone):
                contacts[new_phone] = contacts.pop(phone_number)
                contacts[new_phone]['phone'] = new_phone
                print("Phone number updated successfully.")
                break
            else:
                print("Invalid phone number format. Please try again.")

    elif edit == "3":
        while True:
            new_email = input("Enter the new email address: ")
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', new_email):
                contacts[phone_number]['email'] = new_email
                print("Email address updated successfully.")
                break
            else:
                print("Invalid email address format. Please try again.")

    elif edit == "4":
        new_address = input("Enter the new address: ")
        contacts[phone_number]['address'] = new_address
        print("Address updated successfully.")

    elif edit == "5":
        new_notes = input("Enter the new notes: ")
        contacts[phone_number]['notes'] = new_notes
        print("Notes updated successfully.")

    else:
        print("Invalid option. Please try again.")
