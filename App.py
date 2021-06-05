
import CRUD
import Interface as inter
import sys


contacts = CRUD.Read()
if not(contacts):
    sys.exit(1)


mainloop = True
while mainloop:
    opcion = inter.menu()

    if opcion == 1:        
        inter.message("-> Adding Contact")
        id, new_contact = inter.menu()
        CRUD.Create(contacts, id, new_contact)        

    elif opcion == 2:
        inter.message("-> Contact List")       
        inter.read_contacts(contacts)              

    elif opcion == 3:
        inter.message("-> Update contact")       
        interface_response = inter.update_contact(contacts)

        if interface_response != False:
            id,updated_contact = interface_response
            CRUD.Update(contacts, id, inter.update_contact)

    elif opcion == 4:
        inter.message("-> Delete contact") 
        id = inter.delete_contact(contacts)
        if id != False:            
            CRUD.Delete(contacts,id)    

    elif opcion == 5:
        inter.message("-> Exit") 
        if CRUD.Write(contacts):
            inter.message("Saved Data.")
        mainloop = False
    
    else:
        inter.message("Invalid option!")