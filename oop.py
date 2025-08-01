class Car:
    total_car=0

    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car += 1

    def chai_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or diesel"
    

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)
        self.batter_size=battery_size

    def fuel_type():
        return "electric charge"

my_tesla=ElectricCar("Tesla","Model S","85kwh")
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

# my_car= Car("Tata","Safari")
# my_car.model="City"
# Car("Tata","Nexon")
# print(safari.fuel_type())

# print(my_car.general_description())
# print(my_car.model)

# print(Car.total_car)

# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)

class Battery:
    def batter_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla=ElectricCarTwo("tesla","model s")
print(my_new_tesla.engine_info())
print(my_new_tesla.batter_info())