from add_contact import contacts

def search_contact():
    # Prompt the user to enter the phone number of the contact to search for
    phone_number = input("Please enter the phone number of the contact to search (format 111-222-3333): ")

    # Check if the contact exists
    if phone_number in contacts:
        # Display the contact information
        print(f"\nContact Information for {phone_number}:")
        for key, value in contacts[phone_number].items():
            print(f"{key.capitalize()}: {value}")
        print()
    else:
        print("Contact not found.")