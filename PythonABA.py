class Contact:
    def __init__(self,name,phno,email):
        self.name = name
        self.phno = phno
        self.email = email

contact_book = {}

while True:
    print("\n=================================================")
    print("--- CONTACT BOOK SYSTEM ---")
    print("=================================================")
    print("1. Add New Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Exit Application")
    print("=================================================")
    
    choice = int(input("Enter your choice (1-6): "))
    
    if choice == 1:
        print("\n--- ADD NEW CONTACT ---")
        name = input("Enter the Name: ")
        phno = input("Enter the Phone Number: ")
        email = input("Enter the E-mail: ")
        
        new_contact = Contact(name,phno,email)
        
        contact_book[name] = new_contact
        print("\nContact saved successfully!")
        
    elif choice == 2:
        print("\n--- SEARCH CONTACT ---")
        search = input("Enter the name to search: ")
        
        if search in contact_book:
            matched_contact = contact_book[search]
            
            print("\n         CONTACT FOUND                  ")
            print("----------------------------------------")
            print("Name:     ", matched_contact.name)
            print("Phone No: ", matched_contact.phno)
            print("E-mail:   ", matched_contact.email)
            print("----------------------------------------")
        else:
            print("\nError: Contact not found.")
            
    elif choice == 3:
        if not contact_book:
            print("\nThe contact book is empty.")
        else:
            print("\n=================================================")
            print("                      MY CONTACT BOOK                       ")
            print("==================================================")
            print("NAME                 | PHONE                 | EMAIL")
            print("-----------------------------------------------------")
            
            for contact in contact_book.values():
                print(contact.name, "                |", contact.phno, "                |", contact.email)
                
            print("=====================================================")
            
    elif choice == 4:
        print("\n--- UPDATE CONTACT NUMBER ---")
        update = input("Enter the name of the contact to update: ")
        
        if update in contact_book:
            new_phno = int(input("Enter the new phone number: "))
            contact_book[update].phno = new_phno
            print("\nContact number updated successfully!")
        else:
            print("\nError: Contact not found.")
            
    elif choice == 5:
        print("\n--- DELETE CONTACT ---")
        delete = input("Enter the name of the contact to delete: ")
        
        if delete in contact_book:
            del contact_book[delete]
            print("\nContact deleted successfully!")
        else:
            print("\nError: Contact not found.")
            
    elif choice == 6:
        print("\nExiting Contacts.")
        break
        
    else:
        print("\nInvalid input! Please enter a number between 1 and 6.")