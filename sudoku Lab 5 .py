# Initial Sudoku grid
grid=[
    [8,1,0,6,7,9,3,4,2],
    [0,9,0,5,0,3,7,1,8],
    [0,3,2,1,4,0,6,5,9],
    [4,8,3,7,0,0,5,0,1],
    [1,2,0,4,8,5,9,7,3],
    [9,0,7,0,3,1,0,6,4],
    [3,0,1,0,0,7,0,0,6],
    [5,0,9,0,0,2,4,3,7],
    [2,7,0,3,6,4,0,0,5],
]
# The answer to the Sudoku grid
ans=[
    [8,1,5,6,7,9,3,4,2],
    [6,9,4,5,2,3,7,1,8],
    [7,3,2,1,4,8,6,5,9],
    [4,8,3,7,9,6,5,2,1],
    [1,2,6,4,8,5,9,7,3],
    [9,5,7,2,3,1,8,6,4],
    [3,4,1,9,5,7,2,8,6],
    [5,6,9,8,1,2,4,3,7],
    [2,7,8,3,6,4,1,9,5],
]
#main
#While true is a forever loop until a condition is meat
while True:
    # returning a value for each row in the gird
    for row in grid:
        # Print function is stripping the brackets
        print(" ".join(map(str, row)))
    #input x3
    #Try function is testing the code for any errors
    try:
        n = int(input(""))
        r = int(input(""))-1
        c = int(input(""))-1
        #virajidate answer
        # The if statement is checking if the condition and execute if it is true
        if n == ans[r][c] and grid[r][c]==0:
            grid[r][c]=n
           # Else function is used to execute both true and false conditions.
        else:
            # print statement is printing an error as the condition is not meat
            print("error")
        #board completion
        # The if statement is checking if the condition and execute if it is true
        if grid == ans:
            # print function is printing game completed if all functions are meat
            print("game complete")
            # break function is used to exit a loop
            break
            # The else function is used to execute both true and false conditions.
        else:
            continue
    # check number input valid
    except:
        # The if statement is checking if the condition and execute if it is true
        if n==0 or n>9:
            print("error")
            continue