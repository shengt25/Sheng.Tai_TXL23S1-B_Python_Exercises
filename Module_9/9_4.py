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


def race(cars):
    hour = 0
    while True:
        # Drive for one hour
        hour += 1
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

        # Check if any car has travelled more than 10000 km
        for car in cars:
            if car.travelled_distance >= 10000:
                return hour


# Creating the cars
cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    cars.append(Car(f"ABC-{i}", max_speed))

# Racing
hour = race(cars)

# Print the results
print(f"Time passed: {hour} hours")
print(f"{'Registration number':<30}{'Max speed':<20}{'Current Speed':<20}{'Travelled distance'}")
for car in cars:
    print(f"{car.registration_number:<30}{car.max_speed:<20}{car.current_speed:<20}{car.travelled_distance}")
