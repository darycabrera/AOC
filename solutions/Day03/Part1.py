# Answer: 8243
import sys


def get_item_priority(item):
    """
    converts character to priority value
    """
    if item.islower():
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


with open(sys.argv[1], "r", encoding="ascii") as fl:
    priority_sum = 0
    for line in fl:
        rucksack = line.strip()
        size = len(rucksack)
        first_compartment_set = set(rucksack[0 : size // 2])
        second_compartment_set = set(rucksack[size // 2 :])
        duplicate_item = first_compartment_set.intersection(
            second_compartment_set
        ).pop()
        priority_sum += get_item_priority(duplicate_item)
    print(priority_sum)
