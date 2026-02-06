

class Car:

    def __init__(self, price, model):
        self.price = price
        self.model = model
        print("Car object created with price:", self.price, "and model:", self.model)

    def brakes(self):
        print("Braking")

    def speed(self):
        print("Accelerating")
z = Car
a = Car(10, "BMW")
b = Car(20, "Audi")
#printing memory address of the objects
print(z)
print(a)
print(b)