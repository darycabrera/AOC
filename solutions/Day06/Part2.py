# Answer 3425
import sys

with open(sys.argv[1], "r", encoding="ascii") as fl:
    for line in fl:
        running_fourteen = line[0:14]
        potential_marker = set(running_fourteen)
        index = 14
        for ch in line[14:].strip():
            if len(potential_marker) == 14:
                print(index)
                break
            else:
                running_fourteen = running_fourteen[1:14] + ch
                potential_marker = set(running_fourteen)
                index += 1
