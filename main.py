from ui import print_ui
from add_contact import contacts, add_contact
from edit_contact import edit_contact
from delete_contact import delete_contact
from search_contact import search_contact
from display_contact import display_contact
from export_contacts import export_contacts_to_file
from import_contacts import import_contacts_from_file

run = True

while run is True:
    print_ui()
    action = int(input("What would you like to perform? "))
    if action == 1:
        add_contact()
    elif action == 2:
        edit_contact()
    elif action == 3:
        delete_contact()
    elif action == 4:
        search_contact()
    elif action == 5:
        display_contact()
    elif action == 6:
        export_contacts_to_file()
    elif action == 7:
        import_contacts_from_file()
    elif action == 8:
        print("Thank you for using contact management system. ")
        run = False
    else:
        print("Invalid reponse, please try again.")
    

    