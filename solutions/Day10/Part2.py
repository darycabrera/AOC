# Answer:
#   ###..####..##..###..#..#.###..####.###..
#   #..#....#.#..#.#..#.#.#..#..#.#....#..#.
#   #..#...#..#....#..#.##...#..#.###..###..
#   ###...#...#.##.###..#.#..###..#....#..#.
#   #....#....#..#.#....#.#..#....#....#..#.
#   #....####..###.#....#..#.#....####.###..
import sys


def update_pixel(display, num_cells, row_length, iteration, sprite_position):
    # After entire display populates, the next display cycle begins
    pixel_id = iteration % num_cells
    # Calculate pixel to update in display
    row = pixel_id // row_length
    col = pixel_id % row_length
    pixel_offset = abs(col - sprite_position)
    if pixel_offset <= 1:
        # Pixel overlaps with sprite that is 3 pixels in length. Light it.
        display[row][col] = "#"


with open(sys.argv[1], "r", encoding="ascii") as fl:
    instructions = (line.strip().split() for line in fl)
    sprite_middle_index = 1
    current_cycle = 0
    rows, cols = (6, 40)
    total_pixels = rows * cols
    # Initialize a dark display for crt
    crt = [["." for i in range(cols)] for j in range(rows)]
    for instruction in instructions:
        if instruction[0] == "addx":
            update_pixel(crt, total_pixels, cols, current_cycle, sprite_middle_index)
            current_cycle += 1
            update_pixel(crt, total_pixels, cols, current_cycle, sprite_middle_index)
            current_cycle += 1
            sprite_middle_index += int(instruction[1])
        else:
            # Noop
            update_pixel(crt, total_pixels, cols, current_cycle, sprite_middle_index)
            current_cycle += 1
    # Dump display
    for r in crt:
        print("".join(r))
