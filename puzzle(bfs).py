import copy
from heapq import heappush, heappop

# Size of the puzzle (3 for 8-puzzle, 4 for 15-puzzle, etc.)
n = 3

# Directions for moving the empty tile: down, left, up, right
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, node):
        heappush(self.heap, node)

    def pop(self):
        return heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

class Node:
    def __init__(self, parent, state, empty_tile_pos, cost, level):
        self.parent = parent
        self.state = state
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level

    def __lt__(self, other):
        return (self.cost + self.level) < (other.cost + other.level)

def calculate_cost(state, goal_state):
    count = 0
    for i in range(n):
        for j in range(n):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

def create_new_node(state, empty_tile_pos, new_empty_tile_pos, level, parent, goal_state):
    new_state = copy.deepcopy(state)
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]

    cost = calculate_cost(new_state, goal_state)
    return Node(parent, new_state, new_empty_tile_pos, cost, level)

def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()

def is_valid_pos(x, y):
    return 0 <= x < n and 0 <= y < n

def print_solution_path(node):
    if node is None:
        return
    steps = 0
    path = []
    while node:
        path.append(node)
        node = node.parent
        steps += 1
    path.reverse()
    for step in path:
        print_state(step.state)
    return steps - 1  # Subtracting 1 because we count steps, not nodes

def solve_puzzle(initial_state, empty_tile_pos, goal_state, max_iterations=10000):
    pq = PriorityQueue()
    initial_cost = calculate_cost(initial_state, goal_state)
    root = Node(None, initial_state, empty_tile_pos, initial_cost, 0)
    pq.push(root)

    visited = set()
    iterations = 0

    while not pq.is_empty():
        iterations += 1
        if iterations > max_iterations:
            print("Can't solve the puzzle. Exceeded maximum iterations.")
            return

        current_node = pq.pop()
        state_tuple = tuple(tuple(row) for row in current_node.state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        print(f"Current node cost: {current_node.cost}, level: {current_node.level}")  # Debug print

        if current_node.cost == 0:
            steps = print_solution_path(current_node)
            print(f"Puzzle solved in {steps} steps.")
            print("Final state:")
            print_state(current_node.state)
            return

        x, y = current_node.empty_tile_pos
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if is_valid_pos(new_x, new_y):
                child_node = create_new_node(current_node.state, (x, y), (new_x, new_y), current_node.level + 1, current_node, goal_state)
                pq.push(child_node)

    print("Can't solve the puzzle.")

# Read the initial state from the user
initial_state = []
print("Enter the initial state (3x3 matrix, use 0 for the empty space):")
for _ in range(n):
    row = list(map(int, input().split()))
    initial_state.append(row)

# Read the goal state from the user
goal_state = []
print("Enter the goal state (3x3 matrix, use 0 for the empty space):")
for _ in range(n):
    row = list(map(int, input().split()))
    goal_state.append(row)

# Find the initial position of the empty tile
empty_tile_pos = None
for i in range(n):
    for j in range(n):
        if initial_state[i][j] == 0:
            empty_tile_pos = (i, j)
            break
    if empty_tile_pos:
        break

print(f"Initial state: {initial_state}")  # Debug print
print(f"Goal state: {goal_state}")  # Debug print
print(f"Empty tile position: {empty_tile_pos}")  # Debug print

# Solve the puzzle
solve_puzzle(initial_state, empty_tile_pos, goal_state)