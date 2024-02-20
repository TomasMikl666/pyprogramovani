# class Fruit:
#     def __init__(self, name , clr, exp_date):
#         self.name = name
#         self.colour = clr
#         self.exp_date = exp_date
#     def details(self):
#         print(f"my {self.name} is  {self.colour}")
#         print(f"expires on {self.exp_date}")

# apple = Fruit("apple", "red","7.21.2002")
# apple.details()
class Guitar:
    def __init__(self, n_strings=6) -> None:
        self.n_strings = n_strings
        self.play()
        
    def play(self):
        print("pam pam pam pam")
class BassGuitar(Guitar):
    pass
class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__()
        self.n_strings = 8
        self.color = ("#000000", "#FFFFFF")
    def playLouder(self):
        print("pam pam pam pam".upper())
    

my_guitar = ElectricGuitar()
my_guitar.playLouder()

print(BassGuitar(4).n_strings)