# Multiple Inheritance

class Car:
  total_cars = 0

  def __init__(self,brand,model):
    self.__brand = brand
    self.__model = model
    Car.total_cars += 1

  def get_brand(self):
    return self.__brand

  def full_name(self):
    return f"{self.__brand} {self.__model}"

  def fuel_type(self):
    return "Petrol or Disel"  

  @staticmethod
  def general_description():
    return "This is a car, Means of transport"

  @property
  def model(self): 
    return self.__model

class Electric_Car(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"  


my_car = Car("Tata", "Safari")
# print(my_car.general_description())
# my_car.model = "City"
# print(my_car.model)

mytesla = Electric_Car("Tesla", "Model S", "85kWh")

# print(isinstance(mytesla, Car))
# print(isinstance(mytesla, Electric_Car))

class Battery:
  def battery_info(self):
    return "Battery Information"
  

class Engine:
  def engine_info(self):
    return "Engine Information"

class ElectricCarTwo(Battery, Engine, Car):
  pass

my_new_tesla = ElectricCarTwo("tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
