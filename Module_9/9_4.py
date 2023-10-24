import random


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


cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    cars.append(Car(f"ABC-{i}", max_speed))
hour = 0

end_loop = False
while True:
    hour += 1
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

    for car in cars:
        # If any car has travelled more than 10000 km, stop immediately
        if car.travelled_distance >= 10000:
            end_loop = True

    if end_loop:
        break

print(f"Time passed: {hour} hours")
print(f"{'Registration number':<30}{'Max speed':<30}{'Current Speed':<30}{'Travelled distance'}")
for car in cars:
    print(f"{car.registration_number:<30}{car.max_speed:<30}{car.current_speed:<30}{car.travelled_distance}")

