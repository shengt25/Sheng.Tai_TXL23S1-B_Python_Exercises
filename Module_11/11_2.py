class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity
        self.battery_charge = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, fuel_capacity):
        super().__init__(registration_number, max_speed)
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity


# Creating cars
electric_car1 = ElectricCar("ABC-15", 180, 52.5)
gasoline_car1 = GasolineCar("ABC-123", 165, 32.3)

# Setting speeds
electric_car1.current_speed = 100
gasoline_car1.current_speed = 120

# Driving cars
electric_car1.drive(3)
gasoline_car1.drive(3)

# Print the results
print(f"Electric car speed: {electric_car1.current_speed}")
print(f"Gasoline car speed: {gasoline_car1.current_speed}")
print("\nAfter 3 hours:")
print(f"Electric car {electric_car1.registration_number} travelled {electric_car1.travelled_distance} km")
print(f"Gasoline car {gasoline_car1.registration_number} travelled {gasoline_car1.travelled_distance} km")
