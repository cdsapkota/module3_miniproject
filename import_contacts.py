from add_contact import contacts

def import_contacts_from_file():
    # Prompt the user for the filename
    filename = input("Please enter the filename to import contacts from (e.g., contacts.txt): ")
    
    try:
        with open(filename, "r") as file:
            current_contact = {}
            phone_number = None

            # Read the file line by line
            for line in file:
                line = line.strip()  # Remove any surrounding whitespace or newline characters

                if line.startswith("Phone Number:"):
                    # If there is a current contact being built, save it before starting a new one
                    if phone_number and current_contact:
                        contacts[phone_number] = current_contact
                        current_contact = {}

                    # Extract the phone number from the line
                    phone_number = line.split("Phone Number: ")[1].strip()

                elif line.startswith("Name:"):
                    current_contact['name'] = line.split("Name: ")[1].strip()

                elif line.startswith("Email:"):
                    current_contact['email'] = line.split("Email: ")[1].strip()

                elif line.startswith("Address:"):
                    current_contact['address'] = line.split("Address: ")[1].strip()

                elif line.startswith("Notes:"):
                    current_contact['notes'] = line.split("Notes: ")[1].strip()

            # Save the last contact in the file
            if phone_number and current_contact:
                contacts[phone_number] = current_contact

        print(f"Contacts successfully imported from {filename}")

    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred while importing contacts: {e}")