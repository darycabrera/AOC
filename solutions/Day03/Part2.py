# Answer: 2631
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
    group_sack_count = 0
    group_rucksacks = []
    for line in fl:
        group_rucksacks.append(set(line.strip()))
        group_sack_count += 1
        if group_sack_count == 3:
            shared_item = (
                group_rucksacks[0]
                .intersection(group_rucksacks[1], group_rucksacks[2])
                .pop()
            )
            priority_sum += get_item_priority(shared_item)
            group_sack_count = 0
            group_rucksacks = []
    print(priority_sum)
