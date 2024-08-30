class User():
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"Attacking with power of {self.power}")


wizard1 = Wizard('Zac', 50, "zac@gmail.com")
print(wizard1.email)

print(dir(wizard1))
