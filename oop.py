class Car:
    total_car=0

    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        Car.total_car += 1

    def chai_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or diesel"
    
    def general_description(self):
        return "Cars are means of transport"
    
class ElectricCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)
        self.batter_size=battery_size

    def fuel_type():
        return "electric charge"

# my_tesla=ElectricCar("Tesla","Model S","85kwh")
# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

my_car= Car("Tata","Safari")
Car("Tata","Nexon")
# print(safari.fuel_type())

print(my_car.general_description())
print(Car.general_description())

# print(Car.total_car)

# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)