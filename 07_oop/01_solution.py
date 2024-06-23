# Basic Class and Object

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

my_car = Car("Toyata", "voraolla")
print(my_car.brand)

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)
