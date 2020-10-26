grid9 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grid91 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 1, 4, 3, 6, 5, 8, 9, 7],
    [3, 6, 5, 8, 9, 7, 2, 1, 4],
    [8, 9, 7, 2, 1, 4, 3, 6, 5],
    [5, 3, 1, 6, 4, 2, 9, 7, 8],
    [6, 4, 2, 9, 7, 8, 5, 3, 1],
    [9, 7, 8, 5, 3, 1, 6, 4, 2],
]


def evaluate(grid, y, x, n):

    a = len(grid)

    # check row

    for i in range(0, a):
        if grid[i][x] == n:
            return False

    # check column

    for i in range(0, a):
        if grid[y][i] == n:
            return False

    # check square

    x_0 = x // 3
    y_0 = y // 3

    for row in range(y_0 * 3, (y_0 * 3) + 3):
        for col in range(x_0 * 3, (x_0 * 3) + 3):
            if grid[row][col] == n:
                return False
    return True


def look_for_zeros(grid):
    a = len(grid)
    for y in range(0, a):
        for x in range(0, a):
            if grid[y][x] == 0:
                return True
            else:
                continue
    return False


def solve(grid, allsolutions):

    if not look_for_zeros(grid):
        return True
    a = len(grid)
    for y in range(a):
        for x in range(a):
            if grid[y][x] == 0:
                for n in range(1, a + 1):
                    if evaluate(grid, y, x, n):
                        grid[y][x] = n
                        if solve(grid, allsolutions):
                            if len(allsolutions) == 0:
                                allsolutions.append(grid)
                                return True
                            elif compare_solutions(
                                grid, allsolutions
                            ):  # erkennt nicht ob selber generiert Loesung oder alte Loesung
                                allsolutions.append(grid)
                                return True
                            else:
                                return False
                        grid[y][x] = 0
                return


def print_grid(grid):
    a = len(grid)
    for i in range(a):
        print(grid[i])


def compare_solutions(grid, allsolutions):
    if len(allsolutions) == 0:
        return True
    for i in range(len(allsolutions)):
        if grid == allsolutions[i]:
            return False
    return True


allsolutions = []

print_grid(grid9)
print("")

solve(grid9, allsolutions)
for j in range(len(allsolutions)):
    for i in range(9):
        print(allsolutions[j][i])

print(" ")

solve(grid9, allsolutions)

for j in range(len(allsolutions)):
    for i in range(9):
        print(allsolutions[j][i])
