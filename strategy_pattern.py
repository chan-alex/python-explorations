
# Strategy pattern is a method of encapsulating a set of algorithms
# that can be used interchangely depending on stituation.

# this is a simple example of the strategy pattern.


def basic_display(msg):
    print(msg)

def html_display(msg):
    print("<p>")
    print(msg)
    print("</p>")


def boxed_display(msg):
    msg_length = len(msg)

    horizontal_line = (msg_length + 2) * "="
    print(horizontal_line)
    print("|" + msg + "|")
    print(horizontal_line)    

def test():

    message = "This is important message"

    print("Stategy #1:")
    display_method = basic_display
    display_method(message)
    print("")

    print("Stategy #2:")
    display_method = html_display
    display_method(message)
    print("")
    
    print("Stategy #3:")    
    display_method = boxed_display
    display_method(message)
    print("")
