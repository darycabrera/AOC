# Answer 51382025916
import sys
import math


class Monkey(object):
    def __init__(
        self,
        identity,
        items,
        operation,
        test_function,
        divider,
        positive_monkey_id,
        negative_monkey_id,
        inspections=0,
    ):
        self.identity = identity
        self.items = items
        self.operation = operation
        self.test_function = test_function
        self.divider = divider
        self.positive_monkey_id = positive_monkey_id
        self.negative_monkey_id = negative_monkey_id
        self.inspections = inspections

    def __repr__(self):
        return (
            f"Monkey {self.identity}:\n"
            + f"\tItems: {self.items}\n"
            + f"\tOperation: {self.operation}\n"
            + f"\tTest: {self.test_function}\n"
            + f"\t\tTrue throw: {self.positive_monkey_id}\n"
            + f"\t\tFalse throw: {self.negative_monkey_id}\n"
            + f"\tInspections: {self.inspections}\n"
        )


def parse_monkey(structure):
    # Read Monkey Header
    args = structure[0].split()
    monkey_id = int(args[1].rstrip(":"))

    # Read Monkey's possessions
    args = structure[1].split(": ")[1].split(", ")
    monkey_items = [int(i) for i in args]

    # Read monkey's M.O.
    operator, operand = structure[2].split()[-2:]
    if operator == "*":
        if operand == "old":
            monkey_operation = lambda a: a * a
        else:
            monkey_operation = lambda a: a * int(operand)
    else:
        # Only multiplication and addition supported
        monkey_operation = lambda a: a + int(operand)

    # Read test
    monkey_divider = int(structure[3].split()[-1])
    monkey_bool_test = lambda a: not bool(a % monkey_divider)

    # Read positive test case
    positive_monkey_id = int(structure[4].split()[-1])

    # Read negative test case
    negative_monkey_id = int(structure[5].split()[-1])

    return Monkey(
        monkey_id,
        monkey_items,
        monkey_operation,
        monkey_bool_test,
        monkey_divider,
        positive_monkey_id,
        negative_monkey_id,
    )


monkeys = []
with open(sys.argv[1], "r", encoding="ascii") as fl:
    monkey_input = []
    for line in fl:
        if line.isspace():
            monkeys.append(parse_monkey(monkey_input))
            monkey_input = []
        else:
            monkey_input.append(line.strip())
    # Parse last monkey
    monkeys.append(parse_monkey(monkey_input))

rounds = int(sys.argv[2])

# Get product of all dividers. This is how we keep worry levels managable
magic_number = math.prod(monkey.divider for monkey in monkeys)

while rounds > 0:
    for monkey in monkeys:
        for item in monkey.items:
            worry_level = monkey.operation(item) % magic_number
            if monkey.test_function(worry_level):
                # If worry is divisible by monkey's divider,
                # throw item to positive monkey's collection
                monkeys[monkey.positive_monkey_id].items.append(worry_level)
            else:
                # throw item to negative monkey's collection
                monkeys[monkey.negative_monkey_id].items.append(worry_level)
        monkey.inspections += len(monkey.items)
        # Monkey has thrown all items
        monkey.items = []
    rounds -= 1

for monkey in monkeys:
    print(f"Monkey {monkey.identity}: {monkey.items}")
    print(f"Monkey {monkey.identity} inspected {monkey.inspections} items")

# Get two most active monkeys
monkeys.sort(reverse=True, key=lambda m: m.inspections)
most_active_monkeys = monkeys[0:2]
print("Two Most Active Monkeys:")
for monkey in most_active_monkeys:
    print(f"  Monkey {monkey.identity} inspected {monkey.inspections} items")

print(
    f"Monkey Business Level: {most_active_monkeys[0].inspections * most_active_monkeys[1].inspections}"
)
