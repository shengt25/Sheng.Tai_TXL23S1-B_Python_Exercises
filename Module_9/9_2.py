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


my_car = Car("ABC-123", 142)

my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)
print(f"Current speed: {my_car.current_speed} km/h")
my_car.accelerate(-200)
print(f"Current speed: {my_car.current_speed} km/h")
