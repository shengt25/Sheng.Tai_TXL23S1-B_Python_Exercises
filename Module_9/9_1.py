class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


my_car = Car("ABC-123", 142)

print("The properties of my car:\n")
print(f"Registration number: {my_car.registration_number}")
print(f"Max speed: {my_car.max_speed} km/h")
print(f"Current speed: {my_car.current_speed} km/h")
print(f"Travelled distance: {my_car.travelled_distance} km")
