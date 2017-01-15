

class ContactList(list):

    def print_all(self):
        for c in self:
            print(c)


class Contact:
    contact_list = ContactList() 

    def __init__(self, name):
        self.name = name
        self.info = []
        self.contact_list.append(self)

    def __str__(self):
        output = "Name: {}\n".format(self.name) 

        for i in self.info:
            output += i.__str__()
            output += '\n'
        
        return output


    def add_info(self,info):
        self.info.append(info)


class PhoneNumber:

    def __init__(self,phone_num):
        self.phone_num = phone_num
        
    def __str__(self):
        output = "Phone Number: {}".format(self.phone_num)
        return output
        
    

if __name__ == "__main__":


    print("start")
    
    c = Contact("alex")
    pn = PhoneNumber("1234567")

    c.add_info(pn)

    print(c)
    


