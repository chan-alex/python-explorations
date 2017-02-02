

# The command pattern represent actions as objects.
# Provides an extraction between actions that need to be done and the object
# that invokes those actions usually at a later time.


# One application of this pattern is in GUI programs.

# The pythonic approach makes use of the fact that the function are 1st class
# object in python.

class Dialog:

    def __init__(self, dialog_name):
        self.name = dialog_name

    def open(self):
        print("Dialog opened. Name = {} ". format(self.name))


    def close(self):
        print("Dialog closed. Name = {} ". format(self.name))        




class toolbar_item:

    def execute(self):
        self.command()




def test():

    dialog1 = Dialog("dialog1")

    open_button = toolbar_item()
    open_button.command = dialog1.open

    close_button = toolbar_item()
    close_button.command = dialog1.close

    
    open_button.execute()
    close_button.execute()    



