from copy import deepcopy

grid9 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

grid0 = deepcopy(grid9)


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
                            if compare_solutions(grid, allsolutions):
                                return True
                            else:
                                grid[y][x] = 0
                                return False
                        grid[y][x] = 0
                return False


def print_grid(grid):
    a = len(grid)
    print("")
    for i in range(a):
        print(grid[i])
    print(" ")


def compare_solutions(grid, allsolutions):
    if len(allsolutions) == 0:
        return True
    for i in range(len(allsolutions)):
        if grid == allsolutions[i]:
            return False
    return True


def solveall(grid, grid0, allsolutions):
    if len(allsolutions) == 20:
        return True
    grid = deepcopy(grid0)
    if solve(grid, allsolutions):
        allsolutions.append(grid)
        if solveall(grid, grid0, allsolutions):
            return True


def print_allsolutions(allsolutions):

    for i in range(len(allsolutions)):
        print("")
        for j in range(len(allsolutions[i])):
            print(allsolutions[i][j])


def checkoutput(allsolutions):
    for i in range(len(allsolutions)):
        for j in range(len(allsolutions)):
            if allsolutions[i] == allsolutions[j]:
                if i == j:
                    continue
                return False
    return True


allsolutions = []

sum = 0
for i in range(len(grid9)):
    sum += grid9[i].count(0)
print(sum)

solveall(grid9, grid0, allsolutions)

print(len(allsolutions))

if checkoutput(allsolutions):
    print("jaa")
