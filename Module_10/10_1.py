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


# Creating an elevator
h = Elevator(1, 7)

# Testing elevators
# Going to floor
floor = 6
print(f"Going to floor: {floor}")
h.go_to_floor(floor)

# Going to bottom floor
print("\n")
print(f"Going to bottom floor: {h.bottom_floor}")
h.go_to_floor(h.bottom_floor)
