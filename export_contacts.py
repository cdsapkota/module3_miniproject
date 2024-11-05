from add_contact import contacts

def export_contacts_to_file(filename="contacts.txt"):
    # Check if there are any contacts to export
    if not contacts:
        print("No contacts available to export.")
        return
    
    # Open the file in write mode
    with open(filename, "w") as file:
        # Loop through each contact
        for phone_number, info in contacts.items():
            file.write(f"Phone Number: {phone_number}\n")
            for key, value in info.items():
                file.write(f"{key.capitalize()}: {value}\n")
            file.write("\n")  # Add a newline to separate each contact
    print(f"Contacts successfully exported to {filename}")