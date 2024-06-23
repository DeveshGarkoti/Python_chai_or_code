# Encapsulation

class Car:
  def __init__(self, brand, model):
    self.__brand = brand
    self.model = model

  def get_brand(self):
    return self.__brand + " !"

  def full_name(self):
    return f"{self.__brand} {self.model}"
  

class Electric_Car(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size

mytesla = Electric_Car("Tesla", "Model S", "85kWh")
# print(mytesla.brand)
print(mytesla.get_brand()) # Tesla !