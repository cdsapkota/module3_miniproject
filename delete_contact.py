from add_contact import contacts

def delete_contact():
    # Prompt the user to enter the phone number of the contact to delete
    phone_number = input("Please enter the phone number of the contact to delete (format 111-222-3333): ")

    # Check if the contact exists
    if phone_number in contacts:
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete the contact for {contacts[phone_number]['name']}? (yes/no): ").lower()
        if confirm == 'yes':
            # Delete the contact
            del contacts[phone_number]
            print("Contact deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Contact not found.")