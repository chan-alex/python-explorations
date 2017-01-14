

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

#############################

# This is mixin class. Class that are purely meant to be inherted by other classes        
class WatappsSender:
    def send_watapps(self, message):
        print("Sending watapps message to {} : {}".format(self.telephone, message))

class SMSSender:
    def send_sms(self, message):
        print("Sending sms message to {} : {}".format(self.telephone, message))

        
# This contact inherits from 3 classes
class HandphoneContact(PhoneContact, WatappsSender, SMSSender):
    pass

h = HandphoneContact("Jack", "1234567")

h.send_sms("test")
h.send_watapps("test")
