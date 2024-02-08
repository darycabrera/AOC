# Answer: 207576
import sys

with open(sys.argv[1], "r", encoding="ascii") as fl:
    current_calories = 0
    elf_rations = []
    for line in fl:
        if str.isspace(line):
            elf_rations.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line.rstrip())
    if current_calories > 0:
        elf_rations.append(current_calories)
    elf_rations.sort(reverse=True)

    print(sum(elf_rations[0:3]))
