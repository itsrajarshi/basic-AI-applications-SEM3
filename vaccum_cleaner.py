import random

class VacuumCleanerAI:
    def __init__(self, grid_size, dirt_positions):
        self.grid_size = grid_size
        self.dirt_positions = dirt_positions
        self.position = [0, 0]
        self.cleaned_positions = []

    def detect_dirt(self):
        return self.position in self.dirt_positions

    def move(self):
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up' and self.position[1] > 0:
            self.position[1] -= 1
        elif direction == 'down' and self.position[1] < self.grid_size[1] - 1:
            self.position[1] += 1
        elif direction == 'left' and self.position[0] > 0:
            self.position[0] -= 1
        elif direction == 'right' and self.position[0] < self.grid_size[0] - 1:
            self.position[0] += 1

    def clean(self):
        if self.detect_dirt():
            print(f"Cleaned dirt at position: {self.position}")
            self.cleaned_positions.append(self.position.copy())
            self.dirt_positions.remove(self.position)

    def run(self):
        max_steps = (self.grid_size[0] * self.grid_size[1]) ** 4
        steps = 0
        while self.dirt_positions and steps < max_steps:
            self.move()
            self.clean()
            steps += 1
        if not self.dirt_positions:
            print("All dirt cleaned.")
        else:
            print("Stopped. Max steps reached without cleaning all dirt.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_position(grid_size):
    while True:
        x = get_int_input("Enter x-coordinate: ")
        y = get_int_input("Enter y-coordinate: ")
        if 0 <= x < grid_size and 0 <= y < grid_size:
            return [x, y]
        else:
            print(f"Invalid position. Coordinates must be between 0 and {grid_size-1}.")

grid_size_input = get_int_input("Enter the grid size (n for n x n grid): ")
grid_size = (grid_size_input, grid_size_input)
print(f"Grid Size: {grid_size}")

print("Enter positions for three dirty spots:")
dirt_positions = []
for i in range(3):
    print(f"Spot {i+1}:")
    dirt_positions.append(get_valid_position(grid_size_input))

# Run simulation
vacuum = VacuumCleanerAI(grid_size, dirt_positions)
vacuum.run()
