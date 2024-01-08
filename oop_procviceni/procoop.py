# ==============LOGIKA=====================
class Car:
    #Constructor
    def __init__(self, colour, doors,brand,typ):
        self.colour = colour
        self.doors = doors
        self.brand = brand
        self.typ = typ
        self.distance = 0
        

    def turn_left(self):
        return f"Car {self.brand,self.typ, self.colour}turned left"
    
    def turn_right(self):
        return f"Car {self.brand}, turned right"

    def go_straight(self):
        self.distance += 10
        return f"Auto popojelo o {self.distance} metru"

    def car_distance(self):
        return self.distance
    
    def owner(self,owner_name):
        return f"Vlastníkem auta je: {owner_name}"

class VipCar(Car):
    def __init__(self, colour,doors,brand,typ,password):
        super().__init__(colour, doors,brand,typ)
        self.password = password
        self.software_control = True

    def turn_on_off_software_control(self, turn_on):
        self.software_control = turn_on
        
    def go_straight(self):
        self.distance += 20
        return f"Auto popojelo o {self.distance} metru"

# ===============Použití Logiky============
car1 = Car(colour="red",doors=4,typ="Quattro",brand="Audi")
car2 = Car(colour="green",doors=2,brand="Bugatti",typ="Veyron")
car3 = Car(colour="blue",doors=2,brand="Lamborghini",typ="Urus")

# print(car1.turn_left())
# car2.turn_right()
# car3.go_straight()
# car3.go_straight()
# car3.go_straight()
# print(car3.car_distance())
# print(car1.owner("Pepa"))
# name = input("Zadej jméno vlastníka auta: ")
# print(car2.owner(name))

vip_car1 = VipCar(colour="blue",doors=4,brand="BMW",typ="x6",password="1234")
#print(vip_car1.password)
#print(vip_car1.colour)
#print(vip_car1.turn_left())
# print(vip_car1.software_control)
# vip_car1.turn_on_off_software_control(False)
# print(vip_car1.software_control)
# vip_car1.turn_on_off_software_control(True)
# print(vip_car1.software_control)

print(vip_car1.go_straight())
print(vip_car1.go_straight())
print(vip_car1.distance)