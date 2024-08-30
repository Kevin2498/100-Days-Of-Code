
# Private vs Public Variables
# _variable = private

class PlayerCharacter():

    #Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if(age>18):
            self._name = name  #attributes
            self._age = age

    def run(self, message):
        print(f"{self._name} run {message}")
    
    def shout(self):
        print(f"My name is {self._name}")

    def test(self):
        return self
    
    @classmethod
    def add(cls, name, a, b):
        return cls(name, a+b)
    
    @staticmethod
    def adding_things(a, b):
        return(a+b)


player1 = PlayerCharacter('Kevin', 26)

# player1.name = "!!!!"
# player1.shout = "BOOO"

player1.shout()

# help(PlayerCharacter)
