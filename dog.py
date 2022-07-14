class Dog():
    def __init__(self, name, age):
        self.name=name.title()
        self.age=age
    
    def speak(self):
        return "Bark"

    def change_name(self, name):
        self.name = name.title()
    
    def birthday(self):
        self.age+=1