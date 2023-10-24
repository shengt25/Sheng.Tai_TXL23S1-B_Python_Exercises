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


# Creating an elevator
h = Elevator(1, 7)
print(f"Now you are at: {h.current_floor}")

# Going to floor with user input
try:
    floor = int(input("Enter floor number to go to: "))
except:
    print("Invalid input")
else:
    h.go_to_floor(floor)

# Going to bottom floor
print("\n")
print(f"Now you are at: {h.current_floor}")
print(f"Going to bottom floor: {h.bottom_floor}")
h.go_to_floor(h.bottom_floor)
