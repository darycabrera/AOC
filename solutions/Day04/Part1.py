# Answer 536
import sys


def get_section_id_set(section_range):
    """
    Convert given section ID range to a set of IDs
    """
    assignment = section_range.split("-")
    return set(range(int(assignment[0]), int(assignment[1]) + 1))


with open(sys.argv[1], "r", encoding="ascii") as fl:
    num_complete_overlaps = 0
    for line in fl:
        pair = line.split(",")
        first_elf_assignments = get_section_id_set(pair[0])
        second_elf_assignments = get_section_id_set(pair[1])
        if first_elf_assignments.issuperset(
            second_elf_assignments
        ) or second_elf_assignments.issuperset(first_elf_assignments):
            num_complete_overlaps += 1

    print(num_complete_overlaps)
