# Answer 845
import sys


def get_section_id_set(section_range):
    """
    Convert given section ID range to a set of IDs
    """
    assignment = section_range.split("-")
    return set(range(int(assignment[0]), int(assignment[1]) + 1))


with open(sys.argv[1], "r", encoding="ascii") as fl:
    num_overlaps = 0
    for line in fl:
        pair = line.split(",")
        first_elf_assignments = get_section_id_set(pair[0])
        second_elf_assignments = get_section_id_set(pair[1])
        if first_elf_assignments.intersection(second_elf_assignments):
            num_overlaps += 1

    print(num_overlaps)
