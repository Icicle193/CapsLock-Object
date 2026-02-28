class IOString():

    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter something: ")

    def print_string(self):
        print("Transferring to caps lock or resending caps lock answer", self.str1.upper())

str1 = IOString()

str1.get_String()
str1.print_string()