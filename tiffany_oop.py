class oop():
    def __init__(self):
        self.yourString = ""
    def get_String(self):
        self.yourString=input("Enter your name:")
    def print_String(self):
        print(self.yourString.upper())
yourString = oop()
yourString.get_String()
yourString.print_String()
