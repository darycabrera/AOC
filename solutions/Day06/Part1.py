# Answer 1833
import sys

with open(sys.argv[1], "r", encoding="ascii") as fl:
    for line in fl:
        running_four = line[0:4]
        potential_marker = set(running_four)
        index = 4
        for ch in line[4:].strip():
            if len(potential_marker) == 4:
                print(index)
                break
            else:
                running_four = running_four[1:4] + ch
                potential_marker = set(running_four)
                index += 1
