# The Sudoku grid
grid=[

    [6, 8, 0, 0, 0, 5, 4, 3, 1],
    [0, 0, 7, 9, 0, 4, 2, 6, 5],
    [4, 0, 5, 1, 0, 0, 0, 7, 9],
    [2, 5, 8, 4, 0, 0, 0, 9, 3],
    [0, 0, 0, 0, 9, 0, 1, 0, 4],
    [0, 0, 0, 8, 6, 3, 0, 0, 7],
    [7, 1, 3, 0, 0, 0, 9, 4, 0],
    [0, 9, 0, 6, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 7, 0, 2]
]

# Here is the answer to my Sudoku grid
ans=[
    [6, 8, 9, 7, 2, 5, 4, 3, 1],
    [1, 3, 7, 9, 8, 4, 2, 6, 5],
    [4, 2, 5, 1, 3, 6, 8, 7, 9],
    [2, 5, 8, 4, 7, 1, 6, 9, 3],
    [3, 7, 6, 5, 9, 2, 1, 8, 4],
    [9, 4, 1, 8, 6, 3, 5, 2, 7],
    [7, 1, 3, 2, 5, 8, 9, 4, 6],
    [5, 9, 2, 6, 4, 7, 3, 1, 8],
    [8, 6, 4, 3, 1, 9, 7, 5, 2]
]
#main
while True:
    # Returning a value for each row in the grid
    for row in grid:
        # Print function is stripping the brackets
        print(str(row)[1:-1])

    try:
        # Input
        n = int(input("Enter a number: "))
        r = int(input("Enter the row number: ")) - 1
        c = int(input("Enter the column number: ")) - 1
    except ValueError:
        # Check number input validity
        print("Error: Number must be between 1 and 9.")
        continue

    # Checking if the condition is true
    if n == ans[r][c] and grid[r][c] == 0:
        grid[r][c] = n
    else:
        print("Error: Invalid entry\n.")


    # Board completion check
    if grid == ans:
        print("Game complete well done ")
        break
    else:
        continue


