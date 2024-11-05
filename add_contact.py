import re

# Store contacts
contacts = {}

def add_contact():
    name = input("Please enter full name: ")
    
    
    # Validating phone number and email
    phone_pattern = r'^\d{3}-\d{3}-\d{4}$' 
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
       
    # Validate phone number with a loop
    while True:
        phone_number = input("Please enter the phone number in the format 111-222-3333: ")
        if re.match(phone_pattern, phone_number):
            break  # Valid input; exit the loop
        print("Invalid phone number format. Please try again.")

    # Validate email address with a loop
    while True:
        email_address = input("Please enter the email address: ")
        if re.match(email_pattern, email_address):
            break  # Valid input; exit the loop
        print("Invalid email address format. Please try again.")

    # Prompt for additional details
    address = input("Please enter the address: ")
    notes = input("Please enter any notes: ")

    # Store the contact only after all fields are validated
    contacts[phone_number] = {
        'name': name,
        'email': email_address,
        'address': address,
        'notes': notes
    }
    print("Contact added successfully.")
