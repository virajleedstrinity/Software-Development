# The Sudoku grid
grid=[

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

# Here is the answer to my Sudoku grid
ans=[
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

        # Checking if the condition is true
        if n == ans[r][c] and grid[r][c] == 0:
            grid[r][c] = n
        else:
            print("Error: Invalid entry.")

        # Board completion check
        if grid == ans:
            print("Game complete")
            break
        else:
            continue

    except ValueError:
        # Check number input validity
        if n == 0 or n > 9:
            print("Error: Number must be between 1 and 9.")
            continue
