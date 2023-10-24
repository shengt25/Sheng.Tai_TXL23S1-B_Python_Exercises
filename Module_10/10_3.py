class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = 1

    def floor_up(self):
        self.current_floor += 1
        if self.current_floor > self.top_floor:
            self.current_floor = self.top_floor
        print(f"Current floor: {self.current_floor}")
        return self.current_floor

    def floor_down(self):
        self.current_floor -= 1
        if self.current_floor < self.bottom_floor:
            self.current_floor = self.bottom_floor
        print(f"Current floor: {self.current_floor}")
        return self.current_floor

    def go_to_floor(self, floor):
        if floor > self.top_floor or floor < self.bottom_floor:
            print("Invalid floor")
            return

        while self.current_floor != floor:
            if self.current_floor < floor:
                self.floor_up()
            else:
                self.floor_down()
        print(f"Ding! {self.current_floor} arrived.")
        return self.current_floor


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(number_of_elevators)]

    def run_elevator(self, elevator_number, floor):
        print(f"Running elevator {elevator_number} to floor {floor}")
        self.elevators[elevator_number].go_to_floor(floor)
        return self.elevators[elevator_number].current_floor

    def fire_alarm(self):
        print("Fire alarm!")
        for i in range(self.number_of_elevators):
            self.run_elevator(i, self.bottom_floor)


# Creating a 7 floors building with 5 elevators (0 to 4)
b = Building(1, 7, 5)

# Running the elevators 0, 2 and 4
b.run_elevator(0, 7)
b.run_elevator(2, 3)
b.run_elevator(4, 6)

# Testing fire alarm
print("\nTesting fire alarm!")
b.fire_alarm()
