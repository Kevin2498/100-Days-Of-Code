
class PlayerCharacter:

    #Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if(age>18):
            self.name = name  #attributes
            self.age = age

    def run(self, message):
        print(f"{self.name} run {message}")
    
    def shout(self):
        print(f"My name is {self.name}")

    def test(self):
        return self
    
    @classmethod
    def add(cls, name, a, b):
        return cls(name, a+b)
    
    @staticmethod
    def adding_things(a, b):
        return(a+b)


player1 = PlayerCharacter('Kevin', 26)
player1.attack = 75

print(player1.name)
print(player1.age)
print(player1.attack)
print(player1.membership)
player1.run("towards gate1")
player1.shout()
player2 = PlayerCharacter.add("Teddy", 18,2)

print(player2.age)

print(PlayerCharacter.adding_things(8,2))

# player1.name = "!!!!"
# player1.shout = "BOOO"

player1.shout()

# help(PlayerCharacter)
