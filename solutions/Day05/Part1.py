# Answer MQTPGLLDN
import sys

with open(sys.argv[1], "r", encoding="ascii") as fl:
    rows = []
    for line in fl:
        if line.isspace():
            break
        else:
            rows.append(line)

    zeKeys = rows.pop().strip().split()
    column = 1
    stacks = dict()
    for key in zeKeys:
        stack = []
        for row in reversed(rows):
            cell = row[column]
            if not cell.isspace():
                stack.append(cell)
        column += 4
        stacks[key] = stack

    for line in fl:
        tokens = line.split()
        crate_moves = int(tokens[1])
        src_stack = tokens[3]
        dest_stack = tokens[5]
        while crate_moves > 0:
            crate = stacks[src_stack].pop()
            stacks[dest_stack].append(crate)
            crate_moves -= 1

    topCrates = []
    for stack in stacks.values():
        topCrates.append(stack[-1])

    print("".join(topCrates))
