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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        self.hour = 0

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
        self.hour += 1

    def print_status(self):
        print(f"{'Registration number':<30}{'Max speed':<20}{'Current Speed':<20}{'Travelled distance'}")
        for car in self.cars:
            print(f"{car.registration_number:<30}{car.max_speed:<2Z0}{car.current_speed:<20}{car.travelled_distance}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


# Creating the cars
cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    cars.append(Car(f"ABC-{i}", max_speed))

# Creating the race
race = Race("Grand Demolition Derby", 8000, cars)


print(f"Race {race.name} started!")
# Race loop
while True:
    # Drive for one hour
    race.hour_passes()

    # Print status every 10 hours
    if race.hour % 10 == 0:
        print(f"\nRacing time: {race.hour} hours")
        race.print_status()

    # Check is finished
    if race.race_finished():
        # Print final status and exit loop
        print(f"\nRace finished at {race.hour} hours!")
        print(f"Final results of {race.name}:")
        race.print_status()
        break

