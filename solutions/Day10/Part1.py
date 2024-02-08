# Answer ????
import sys


def update(ssi, iteration, val):
    # Calculate cycle with offset
    adjusted_cycle = iteration + 20
    # Get signal every 40 cycles
    if adjusted_cycle % 40 == 0:
        print(f"Cycle {iteration}: {val}")
        ssi.append(iteration * val)


with open(sys.argv[1], "r", encoding="ascii") as fl:
    instructions = (line.strip().split() for line in fl)
    x = 1
    current_cycle = 0
    signal_strength_intervals = []
    for instruction in instructions:
        if instruction[0] == "addx":
            current_cycle += 1
            update(signal_strength_intervals, current_cycle, x)
            current_cycle += 1
            update(signal_strength_intervals, current_cycle, x)
            x += int(instruction[1])
        else:
            # Noop
            current_cycle += 1
            update(signal_strength_intervals, current_cycle, x)
    print(f"Total Signal Strength: {sum(signal_strength_intervals)}")
