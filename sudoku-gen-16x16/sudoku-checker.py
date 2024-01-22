import math

def is_valid_sudoku(grid):
    size = len(grid)
    subgrid_size = int(size ** 0.5)

    # Check rows and columns
    for i in range(size):
        row_set = set()
        col_set = set()
        for j in range(size):
            # Check rows
            if grid[i][j] != 0:
                if grid[i][j] in row_set:
                    return False, (i, j)
                row_set.add(grid[i][j])

            # Check columns
            if grid[j][i] != 0:
                if grid[j][i] in col_set:
                    return False, (j, i)
                col_set.add(grid[j][i])

    # Check subgrids
    for i in range(0, size, subgrid_size):
        for j in range(0, size, subgrid_size):
            subgrid_set = set()
            for k in range(subgrid_size):
                for l in range(subgrid_size):
                    if grid[i + k][j + l] != 0:
                        if grid[i + k][j + l] in subgrid_set:
                            return False, (i + k, j + l)
                        subgrid_set.add(grid[i + k][j + l])

    return True, None

def parse_sudoku_string(sudoku_string):
    # Strip whitespace, collapse multiple contiguous spaces to one (regex), and split into rows
    import re
    rows = re.sub(r'\s+', ' ', sudoku_string).strip().splitlines()
    return [[int(cell) for cell in row.split(' ')] for row in rows]

def print_sudoku(array1d):
    size = int(math.sqrt(len(array1d)))

    # Check if the array length is a perfect square
    if size * size != len(array1d):
        print("Invalid Sudoku array: Length is not a perfect square.")
        return

    # Print the Sudoku grid
    for i in range(size):
        for j in range(size):
            index = i * size + j
            print(array1d[index], end=" ")
            if (j + 1) % int(math.sqrt(size)) == 0 and j + 1 < size:
                print("|", end=" ")
        print()
        if (i + 1) % int(math.sqrt(size)) == 0 and i + 1 < size:
            print("-" * (size * 2 + int(math.sqrt(size)) - 1))

if __name__ == "__main__":
    sudoku_string = """
16 10 7 14 5 8 2 15 13 4 3 12 1 11 9 6
5 3 14 13 11 1 9 16 8 12 6 10 4 2 7 15
8 12 6 1 9 7 14 3 2 11 15 16 10 5 13 4
2 4 15 9 10 16 6 13 14 7 1 5 12 8 11 3
14 8 12 7 16 10 5 2 15 13 4 3 6 1 11 9
11 1 5 16 3 14 13 9 12 6 10 8 7 15 2 4
9 6 13 3 15 12 7 14 1 9 8 2 11 16 10 5
15 7 10 4 6 2 1 11 16 5 9 14 13 3 12 8
3 11 16 5 7 13 10 14 4 15 12 6 8 9 1 2
6 9 2 12 1 4 3 6 9 16 14 7 15 10 8 13
10 15 4 8 14 9 12 5 7 13 10 1 3 6 2 16
12 14 1 10 4 3 2 6 11 8 13 9 16 13 5 7
4 5 9 11 8 6 16 1 3 14 2 12 15 13 16 10
7 13 8 6 2 11 15 7 10 1 5 16 14 12 4 3
1 2 11 15 14 5 8 10 6 3 16 4 2 7 13 9
13 16 3 2 12 15 4 8 5 10 7 11 9 14 6 1
    """

    sudoku_grid = parse_sudoku_string(sudoku_string)

    print("Sudoku Grid:")
    #print(sudoku_grid)
    print_sudoku(sudoku_grid)

    is_valid, invalid_position = is_valid_sudoku(sudoku_grid)

    if is_valid:
        print("\nThis Sudoku grid is valid.")
    else:
        print("\nThis Sudoku grid is not valid.")
        print("Invalid position:", invalid_position)
