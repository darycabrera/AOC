# Answer 301392
import sys


def get_inner_tree_scenic_score(tree_grid, x, y, rows, columns):
    height = tree_grid[x][y]
    west_trees_visible = 0
    east_trees_visible = 0
    south_trees_visible = 0
    north_trees_visible = 0

    # Check to the west
    c = y - 1
    while c >= 0:
        west_trees_visible += 1
        if tree_grid[x][c] >= height:
            # tree blocks view
            break
        c -= 1

    # Check to the east
    c = y + 1
    while c < columns:
        east_trees_visible += 1
        if tree_grid[x][c] >= height:
            # tree blocks view
            break
        c += 1

    # Check to the north
    r = x - 1
    while r >= 0:
        north_trees_visible += 1
        if tree_grid[r][y] >= height:
            # tree blocks view
            break
        r -= 1

    # Check to the south
    r = x + 1
    while r < rows:
        south_trees_visible += 1
        if tree_grid[r][y] >= height:
            # tree blocks view
            break
        r += 1

    # Calculate and return scenic score
    return (
        west_trees_visible
        * east_trees_visible
        * north_trees_visible
        * south_trees_visible
    )


with open(sys.argv[1], "r", encoding="ascii") as fl:
    grid = []
    for line in fl:
        grid.append([int(c) for c in line.strip()])

    num_rows = len(grid)
    end_row_index = num_rows - 1
    num_columns = len(grid[0])
    end_column_index = num_columns - 1
    tree_house_scenic_scores = []
    i = 0
    for row in grid:
        j = 0
        for cell in row:
            if i == 0 or i == end_row_index or j == 0 or j == end_column_index:
                # trees on the edges automatically get a scenic score of 0
                tree_house_scenic_scores.append(0)
            else:
                tree_house_scenic_scores.append(
                    get_inner_tree_scenic_score(grid, i, j, num_rows, num_columns)
                )
            j += 1
        i += 1

    print(f"Highest Scenic Score: {max(tree_house_scenic_scores)}")
