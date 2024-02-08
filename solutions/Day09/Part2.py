# Answer 2303
# This is first time I failed a part
# Here's what I got:
# That's not the right answer; your answer is too high.
# Curiously, it's the right answer for someone else;
# you might be logged in to the wrong account or just unlucky.
# In any case, you need to be using your puzzle input.
# If you're stuck, make sure you're using the full input data;
# there are also some general tips on the about page, or you can
# ask for hints on the subreddit.
# Please wait one minute before trying again. (You guessed 2434.) [Return to Day 9]
import sys


class Position(object):
    "Represents an entity's position on a Coordinate Plane"

    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.name}: ({self.x},{self.y})"

    def follow(self, leader):
        horizontal_offset = abs(self.x - leader.x)
        vertical_offset = abs(self.y - leader.y)

        if (
            vertical_offset > 1
            and horizontal_offset == 1
            or horizontal_offset > 1
            and vertical_offset == 1
        ):
            # Perform diagonal movement
            if self.y < leader.y:
                # We are south of leader, move north
                self.update_position("U", 1)
            else:
                # We are north of leader, move south
                self.update_position("D", 1)

            if self.x < leader.x:
                # We are left of leader, move right
                self.update_position("R", 1)
            else:
                # We are right of leader, move left
                self.update_position("L", 1)
        else:
            if horizontal_offset > 1:
                if self.x < leader.x:
                    # We are left of leader, move right
                    self.update_position("R", 1)
                else:
                    # We are right of leader, move left
                    self.update_position("L", 1)

            if vertical_offset > 1:
                if self.y < leader.y:
                    # We are south of leader, move north
                    self.update_position("U", 1)
                else:
                    # We are north of leader, move south
                    self.update_position("D", 1)

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
    chain = [
        Position("H"),
        Position("1"),
        Position("2"),
        Position("3"),
        Position("4"),
        Position("5"),
        Position("6"),
        Position("7"),
        Position("8"),
        Position("9"),
    ]
    # print(repr(chain[-1]))
    tail_position_paper_trail = {chain[-1].get_position()}
    for direction, steps in instructions:
        i = int(steps)
        while i > 0:
            chain[0].update_position(direction, 1)
            current_tail_position = chain[-1].get_position()
            j = 0
            for link in chain[1:]:
                link.follow(chain[j])
                j += 1
            if current_tail_position != chain[-1].get_position():
                # Add previously unseen position
                tail_position_paper_trail.add(chain[-1].get_position())
                # print(repr(chain[-1]))
            i -= 1
    print(f"Number of Unique Tail Positions: {len(tail_position_paper_trail)}")
