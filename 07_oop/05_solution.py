# Polymorphism

class Car:
  def __init__(self,brand,model):
    self.__brand = brand
    self.model = model

  def get_brand(self):
    return self.__brand

  def full_Name(self):
    return f"{self.__brand} {self.model}"

  def fuel_type(self):
    return "Petrol or disel"

class Electric_Car(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"


myTesla = Electric_Car("Tesla", "Model S", "80kWh")
print(myTesla.full_Name()) # Output: Tesla Model S
print(myTesla.get_brand())
print(myTesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())