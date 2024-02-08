# Answer 5907
import sys


class Position(object):
    "Represents an entity's position on a Coordinate Plane"

    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.name}: ({self.x},{self.y})"

    def follow(self, leader, orientation):
        horizontal_offset = abs(self.x - leader.x)
        vertical_offset = abs(self.y - leader.y)

        if vertical_offset > 1 and horizontal_offset == 1:
            # Perform vertical diagonal movement
            # Move vertically first
            self.update_position(orientation, 1)

            if self.x < leader.x:
                # We are left of leader, move right
                self.update_position("R", 1)
            else:
                # We are right of leader, move left
                self.update_position("L", 1)

        elif horizontal_offset > 1 and vertical_offset == 1:
            # Perform horizontal diagonal movement
            # Move horizontally first
            self.update_position(orientation, 1)

            if self.y < leader.y:
                # We are south of leader, move north
                self.update_position("U", 1)
            else:
                # We are north of leader, move south
                self.update_position("D", 1)

        elif horizontal_offset > 1 or vertical_offset > 1:
            self.update_position(orientation, 1)

    def get_position(self):
        return (self.x, self.y)

    def update_position(self, orientation, offset):
        match orientation:
            case "L":
                self.x -= offset
            case "R":
                self.x += offset
            case "U":
                self.y += offset
            case "D":
                self.y -= offset
            case _:
                raise SystemExit(f"Bad direction: {direction}")


with open(sys.argv[1], "r", encoding="ascii") as fl:
    instructions = (line.strip().split() for line in fl)
    head = Position("H")
    tail = Position("T")
    # print(repr(tail))
    tail_position_paper_trail = {tail.get_position()}
    for direction, steps in instructions:
        i = int(steps)
        while i > 0:
            head.update_position(direction, 1)
            tail.follow(head, direction)
            # print(repr(tail))
            # Add previously unseen position
            tail_position_paper_trail.add(tail.get_position())
            i -= 1
    print(f"Number of Unique Tail Positions: {len(tail_position_paper_trail)}")
