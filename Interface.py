
def message(info=''):
    print(f"\n{info}\n")


def menu():
    print("\n>>> Manage your NetWorking <<<\n\n1. Create Contacts\n2. Read Contacts\n3. Update Contact\n4. Delete Contact\n5. Exit\n")

    option = None
    while option == None:
        try:
            option = int(input("\nSelect an option: "))
        except:        
            print("Invalid entry: A numeric option must be entered.")    

    return option


def validate_contact(id, contacts):
    ids = set(contacts.keys())
    
    if id in ids:
        return True
    else:
        return False 


def create_contact():
    id = input("Enter the contact identifier: ")
    name = input("Name: ")
    city = input("City: ")
    email = input("email: ")
    phone_number = input("Phone number: ")

    new_contact = {
                    'name' : name,
                    'city' : city,
                    'email' : email,
                    'phone_number' : phone_number
                }
    return id, new_contact


def update_contact(contacts):   
    id = input("id from contact to update: ")
    
    if validate_contact(id, contacts):
        new_name = str(input('New Name: '))        
        new_city = str(input('New City: '))        
        new_email = str(input('New e-mail: '))        
        new_phone_number = str(input('New Phone number: '))        

        updated_contact = {
                    'new_name' : new_name,
                    'new_city' : new_city,
                    'new_email' : new_email,
                    'new_phone_number' : new_phone_number
                }
        return id,updated_contact

    else: 
        print("Contact to update not found!")
        return False


def delete_contact(contacts):
    id = input("id from contact to delete: ")
    if validate_contact(id, contacts):
        return id
    else:
        print("Contact to delete not found!")
        return False


def read_contacts(contacts):
    for id, contact in contacts.items():    
        print(id,'- ',end='')
        for data_name, data in contact.items():
            print(data, '| ', end='')
        print()

