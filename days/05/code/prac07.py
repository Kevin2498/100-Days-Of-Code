class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }
    
    def __str__(self):
        return f"{self.color}"
    
    def __len__(self):
        return 5
    
    # def __del__(self):
    #     print("Deleted!!!")

    def __call__(self):
        return("Yess??")
    
    def __getitem__(self, i):
        return self.my_dict[i]


action_fig = Toy('red', 0)
print(action_fig.__str__())
print(str(action_fig))
print(len(action_fig))
# del(action_fig)
print(action_fig())
print(action_fig['name'])