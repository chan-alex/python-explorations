

# This class inherits from the python built-in list class
class ContactList(list):

    # This method just does a simple linear search 
    def search(self, name):  
        for contact in self:
            if contact.name == name:
                return contact


class Contact:
    
    # This is a class attribute. Shared by all objects of this class 
    all_contacts = ContactList()  

    def __init__(self, name):
        self.name = name
        self.all_contacts.append(self)  # Append self to class ContactList attribute.


class PhoneContact(Contact):

    def __init__(self, name, telephone):
        super().__init__(name)
        self.telephone = telephone


Contact("john")
Contact("jack")
Contact("jim")
PhoneContact("judy", "1234567")

print(Contact.all_contacts.search("jack").name)
print(Contact.all_contacts.search("judy").name)
print(Contact.all_contacts.search("judy").telephone)

# ContactList is also a list so can use subscript notation.
print(Contact.all_contacts[3].name)
