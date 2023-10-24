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


my_car = Car("ABC-123", 142)
my_car.travelled_distance = 2000
print("The properties of my car:")
print(f"Registration number: {my_car.registration_number}")
print(f"Max speed: {my_car.max_speed} km/h")
print(f"Current speed: {my_car.current_speed} km/h")
print(f"Travelled distance: {my_car.travelled_distance} km")

print("\n")
my_car.current_speed = 60
my_car.drive(1.5)
print(f"Travelling with {my_car.current_speed} km/h for 1.5 hours")
print(f"Travelled distance: {my_car.travelled_distance} km")
