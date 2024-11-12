
grid = [
    [8, 4, 2, 0, 7, 0, 0, 0, 0],
    [9, 0, 0, 1, 6, 4, 0, 0, 0],
    [0, 8, 9, 0, 0, 0, 0, 6, 0],
    [3, 0, 0, 0, 6, 0, 0, 0, 3],
    [2, 0, 0, 8, 0, 3, 0, 0, 1],
    [1, 0, 0, 0, 2, 0, 0, 0, 6],
    [5, 6, 0, 0, 0, 0, 2, 8, 0],
    [4, 0, 0, 4, 1, 9, 0, 0, 5],
    [7, 0, 0, 0, 8, 0, 0, 7, 9]
]
for row in grid:
    print(" ".join(str(num) if num != 0 else '.' for num in row))
def is_save(grid,row,col,num):
    for i in range(9):
        if grid [row][i]==num:
            return False
        for i in range(9):
            if grid[i][col]==num:
                return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
            return True
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 9):
                    if is_save(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True
if solve_sudoku(grid):
    print("\nSolved Sudoku grid:")
    for row in grid:
        print(" ".join(str(num) for num in row))
else:
    print("No solution exists")

