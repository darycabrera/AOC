# Answer: 60883
import sys

with open(sys.argv[1], "r", encoding="ascii") as fl:
    current_calories = 0
    max_calories = 0
    for line in fl:
        if str.isspace(line):
            if current_calories > max_calories:
                maxCalories = current_calories
            current_calories = 0
        else:
            current_calories += int(line.rstrip())
    if current_calories > maxCalories:
        max_calories = current_calories

    print(maxCalories)
