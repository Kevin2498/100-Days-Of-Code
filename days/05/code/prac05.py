class User():
    def sign_in(self):
        print("Logged in")

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"Attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left-{self.num_arrows}")



wizard1 = Wizard('Zac', 50)
archer1 = Archer('Robin', 100)
wizard1.sign_in()
wizard1.attack()
archer1.sign_in()
archer1.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))


def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)
