def print_grid(a, b, monster, pits, gold):
    for i in range(1, 5):
        for j in range(1, 5):
            if i == a and j == b:
                if (a, b) in adjacent_positions(monster):
                    print("🟫", end="")  # Stench near monster
                elif any((a, b) in adjacent_positions(pit) for pit in pits):
                    print("⬜", end="")  # Breeze near pit
                else:
                    print("📍", end="")  # Player position
            elif (i, j) == monster:
                print("🟥", end="")  # Monster
            elif (i, j) in pits:
                print("⬛", end="")  # Pit
            elif (i, j) == gold:
                print("🟨", end="")  # Gold
            else:
                print("🟩", end="")  # Empty safe cell
        print()
    print()

def adjacent_positions(position):
    x, y = position
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def move(a, b, monster, pits, gold):
    while True:
        s = input("Enter move (u=up, d=down, l=left, r=right): ").lower()

        new_a, new_b = a, b
        if s == "u":
            new_a -= 1
        elif s == "d":
            new_a += 1
        elif s == "l":
            new_b -= 1
        elif s == "r":
            new_b += 1
        else:
            print("Invalid input! Please enter u/d/l/r.")
            continue

        # Check boundaries
        if not (1 <= new_a <= 4 and 1 <= new_b <= 4):
            print("Cannot move outside the grid!")
            continue

        # Check outcomes
        if (new_a, new_b) == gold:
            print_grid(new_a, new_b, monster, pits, gold)
            print("🎉 Congratulations! You found the gold and won the game!")
            return
        elif (new_a, new_b) == monster:
            print_grid(new_a, new_b, monster, pits, gold)
            print("💀 Game over! You were eaten by the monster.")
            return
        elif (new_a, new_b) in pits:
            print_grid(new_a, new_b, monster, pits, gold)
            print("💀 Game over! You fell into a pit.")
            return
        else:
            a, b = new_a, new_b
            print_grid(a, b, monster, pits, gold)

# Initial positions and setup
a, b = 1, 1
monster = (1, 3)
pits = [(3, 1), (3, 3), (4, 4)]
gold = (4, 2)

print_grid(a, b, monster, pits, gold)
move(a, b, monster, pits, gold)
