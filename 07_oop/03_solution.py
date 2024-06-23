# Inhertance

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def full_name(self):
    return f"{self.brand} {self.model}"
  

class ElectriCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size


my_tesla = ElectriCar("Tesla", "model S", "85KWh")
print(my_tesla.full_name())

my_class = Car("Toyata", "Safari")
print(my_class.full_name())