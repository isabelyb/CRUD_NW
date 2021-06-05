import json


def Create(contacts, id, new_contact):    
    contacts[id] = new_contact


def Read(file_path='people.json'):
    dict_contacts = {}
    try:    
        with open(file_path) as file:
            dict_contacts = json.load(file)
    except:
        print("Failed to load data layer")
        return False

    return dict_contacts


def Update(contacts, id, updated_contact): 
    for id_data, data in updated_contact.items():        
        if data:
            contacts[id][id_data] = data


def Delete(contacts, id):
    contacts.pop(id)
    print(f"\n>>> Contact {id} deleted <<<\n")


def Write(contacts, file_path='people.json'):
    try:
        with open(file_path, 'w') as file_json:
            json.dump(contacts, file_json)
    except:
        print("Error: Failed to save information in data layer.")
        return False

    return True