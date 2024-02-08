# Answer 1711
import sys


def is_visible(tree_grid, x, y, rows, columns):
    height = tree_grid[x][y]
    visible = True

    # Check from the west
    c = 0
    while c < y:
        if tree_grid[x][c] >= height:
            visible = False
            break
        c += 1

    if visible:
        # No tree is bigger to the west
        return True
    else:
        visible = True

    # Check to the east
    c = y + 1
    while c < columns:
        if tree_grid[x][c] >= height:
            visible = False
            break
        c += 1

    if visible:
        # No tree is bigger to the east
        return True
    else:
        visible = True

    # Check from the north
    r = 0
    while r < x:
        if tree_grid[r][y] >= height:
            visible = False
            break
        r += 1

    if visible:
        # No tree is bigger to the north
        return True
    else:
        visible = True

    # Check to the south
    r = x + 1
    while r < rows:
        if tree_grid[r][y] >= height:
            visible = False
            break
        r += 1

    return visible


with open(sys.argv[1], "r", encoding="ascii") as fl:
    grid = []
    for line in fl:
        grid.append([int(c) for c in line.strip()])

    num_rows = len(grid)
    end_row_index = num_rows - 1
    num_columns = len(grid[0])
    end_column_index = num_columns - 1
    num_visible_trees = 0
    i = 0
    for row in grid:
        j = 0
        for cell in row:
            if i == 0 or i == end_row_index or j == 0 or j == end_column_index:
                # trees on the edge are visible; don't bother checking
                num_visible_trees += 1
            elif is_visible(grid, i, j, num_rows, num_columns):
                # print(f"visible tree [{i}][{j}] with height {grid[i][j]}")
                num_visible_trees += 1
            j += 1
        i += 1

    print(f"Visible Trees: {num_visible_trees}")
