class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = 1

    def floor_up(self):
        self.current_floor += 1
        if self.current_floor > self.top_floor:
            self.current_floor = self.top_floor
        return self.current_floor

    def floor_down(self):
        self.current_floor -= 1
        if self.current_floor < self.bottom_floor:
            self.current_floor = self.bottom_floor
        return self.current_floor

    def go_to_floor(self, floor):
        if floor > self.top_floor or floor < self.bottom_floor:
            print("Invalid floor")
            return -1

        print(f"Current floor: {self.current_floor}")
        while self.current_floor != floor:
            if self.current_floor < floor:
                self.floor_up()
            else:
                self.floor_down()
            print(f"Current floor: {self.current_floor}")

        print(f"Ding! Floor {self.current_floor} arrived.")
        return self.current_floor


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(number_of_elevators)]

    def run_elevator(self, elevator_number, floor):
        if elevator_number >= self.number_of_elevators:
            print(f"Elevator number {elevator_number} is invalid, it's between 0 and {self.number_of_elevators - 1}")
            return -1
        print(
            f"Running elevator no.{elevator_number}, from floor {self.elevators[elevator_number].current_floor} to {floor}")
        self.elevators[elevator_number].go_to_floor(floor)
        print("\n")
        return self.elevators[elevator_number].current_floor


# Creating a 7 floors building with 5 elevators (from no.0 to no.4)
b = Building(1, 7, 5)

# Testing elevators
# Running the elevators no.0, no.2 and no.4 to floor 7, 3 and 6
b.run_elevator(0, 7)
b.run_elevator(2, 3)
b.run_elevator(4, 6)
