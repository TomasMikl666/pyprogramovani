class WizardPlayer:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age =age

    def attack(self):
        print("utok")
    
    def check_age(self):
        if self.age >= 18:
            print("mužete hrat")
        else:
            print("nizky vek")
    
zadej = input("Zadej jmeno: ")
zadej2 = int(input("Zadej věk:"))

player1= WizardPlayer(zadej,zadej2)
print(player1.name,player1.age)
player1.check_age()

player2= WizardPlayer(zadej,zadej2)
print(player2.name,player2.age)
player2.check_age()