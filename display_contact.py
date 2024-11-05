from add_contact import contacts

def display_contact():
    # Check if there are any contacts to display
    if not contacts:
        print("No contacts available.")
        return
    
    print("All Contacts:\n")
    # Loop through each contact and display its details
    for phone_number, info in contacts.items():
        print(f"Phone Number: {phone_number}")
        for key, value in info.items():
            print(f"{key.capitalize()}: {value}")
        print()