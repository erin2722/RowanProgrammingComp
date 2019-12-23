#Scoring IDs: 2M503, 60M743
# ***********READS IN DATA***********
#input: nothing
#output:  an array with the tile elimination size, the grid, and the moves
def readInData():
    #reads the data in line by line, removes new line character
    boardSize = file.readline().strip('\n')
    boardSize = boardSize.split(' ')
    tileEliminationSize = file.readline().strip('\n')
    numberOfRows = int(file.readline().strip('\n'))
    #now read in the grids
    tempGrid = []
    grid = []
    #read in the grid as it is
    for i in range(0, numberOfRows):
        newRow = file.readline().strip('\n')
        tempGrid.append(newRow.split(' '))
    addedRows = int(boardSize[1]) - numberOfRows

    #reverse the grid so that (0, 0) is equivalent to grid[0][0]
    for i in range(0, len(tempGrid)):
        grid.append(tempGrid[len(tempGrid) - 1 - i])

    #add the extra rows
    for i in range(0, addedRows):
        tempRow = []
        for j in range(0, int(boardSize[0])):
            tempRow.append('-')
        grid.append(tempRow)
    #replace all of the 0s with dashes
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == '0':
                grid[i][j] = '-'

    numberOfMoves = int(file.readline())
    moves = []
    for i in range(0, numberOfMoves):
        move = file.readline().strip('\n')
        move = move.split(' ')
        for i in range(0, len(move)):
            move[i] = int(move[i])
        moves.append(move)

    return [tileEliminationSize, grid, moves, boardSize]


# ***********CARRIES OUT DROPPING***********
# input: a 2D array representing the grid
# output: a 2D array representing the grid after dropping
def dropping(grid):
    # in order to account for the grid being reversed (0 being at the bottom, not the top) we reverse the input grid.
    newGrid = grid[::-1]
    for i in range(0, len(newGrid)-1):
        for j in range(0, len(newGrid[0])-1):
            value = newGrid[i][j]
            # for each row, we iterate through each value:
            #    check if that value is nonzero
            #    check if the value at the same index in the row below is zero
            #    if both of these conditions are met, move the nonzero value down a row
            if (value != "-" and newGrid[i+1][j] == "-"):
                newGrid[i+1][j] = value
                newGrid[i][j] = "-"
    # finally, reverse the grid again to return them in the correct order
    return newGrid[::-1]

# ***********CHECKS FOR DROPS***********
# input: a 2D array representing the grid
# output: boolean representing if it drops or not
def dropCheck(grid):
    # in order to account for the grid being reversed (0 being at the bottom, not the top) we reverse the input grid.
    newGrid = grid[::-1]
    drops = 0
    for i in range(0, len(newGrid)-1):
        for j in range(0, len(newGrid[0])-1):
            value = newGrid[i][j]
            # for each row, we iterate through each value:
            #    check if that value is nonzero
            #    check if the value at the same index in the row below is zero
            #    if both of these conditions are met, move the nonzero value down a row
            if (value != "-" and newGrid[i+1][j] == "-"):
                drops += 1
    # finally, reverse the grid again to return them in the correct order
    return drops


# ***********CHECKS IF HORIZONTAL ELIMINATIONS CAN BE MADE***********
# input: a 2D array representing the grid and an integer representing the deletion length
# output: an array with the row of the elim, the last column of the elim, and the length of the elim
def checkForHorizontalElims(grid, elimLength):
    previousNumber = '0'
    currentLength = 1
    elimLocations = []
    #cycle through the grid
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            #look for consecutive numbers
            if grid[i][j] == previousNumber:
                currentLength += 1
            else:
                #add the elim row to the array if it is long enough and if it is actually of numbers
                if currentLength >= elimLength and previousNumber != "-":
                    elimLocations.append([i, j, currentLength])
                #reset the length of the elim string
                currentLength = 1
            previousNumber = grid[i][j]
        #after the row is done check if it should be added to the elim array one more time
        if currentLength >= elimLength and previousNumber != "-":
            elimLocations.append([i, j, currentLength])
        currentLength = 1
        previousNumber = '0'
    return elimLocations

# ***********CHECKS IF VERTICAL ELIMINATIONS CAN BE MADE***********
# input: a 2D array representing the grid and an integer representing the deletion length
# output: an array with the column of the elim, the last row of the elim, and the length of the elim

def checkForVerticalElims(grid, elimLength):
    previousNumber = '0'
    currentLength = 1
    elimLocations = []
    #same code as the horizontal function but switches columns and rows
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid)):
            if grid[j][i] == previousNumber:
                currentLength += 1
            else:
                if currentLength >= elimLength and previousNumber != "-":
                    elimLocations.append([i, j, currentLength])
                currentLength = 1
            previousNumber = grid[j][i]
        if currentLength >= elimLength and previousNumber != "-":
            elimLocations.append([i, j, currentLength])
        currentLength = 1
        previousNumber = '0'
    return elimLocations


# ***********MAKES HORIZONTAL ELIMINATIONS***********
# input: a 2D array representing the grid and the array from the checkForHorizontalElims function
# output: the new grid
def makeHorizontalElims(grid, elimLocations):
    #does each elim based on the locations array
    if len(elimLocations) == 0:
        return grid
    else:
        for elimCommand in elimLocations:
            row = elimCommand[0]
            endCol = elimCommand[1] + 1
            startCol = endCol - elimCommand[2]
            #replaces each number with a dash
            for i in range(startCol, endCol):
                grid[row][i] = "-"
        return grid

# ***********MAKES VERTICAL ELIMINATIONS***********
# input: a 2D array representing the grid and the array from the checkForVerticalElims function
# output: the new grid
def makeVerticalElims(grid, elimLocations):
    #same as horizontal code but switches rows and columns
    if len(elimLocations) == 0:
        return grid
    else:
        for elimCommand in elimLocations:
            col = elimCommand[0]
            endRow = elimCommand[1] + 1
            startRow = endRow - elimCommand[2]
            for i in range(startRow, endRow):
                grid[i][col] = "-"
        return grid


# ***********CHECKS IF THE BOARD IS CLEAR***********
# input: a 2D array representing the grid
# output: a boolean representing whether the board is clear or not
def checkBoardClear(grid):
    clear = True
    # iterates through every value in the array. if any are numbers, return false.
    for i in range(0, len(grid)):
        for j in range(0,len(grid[0])):
            if (grid[i][j] != "-"):
                clear = False
    return clear


# ***********CHECKS IF THE MOVE IS VALID***********
# input: a 2D array representing the grid and the move as an array with 4 integers: [initCol, initRow, newCol, newRow]
# output: a boolean representing whether the move is valid or not
def isMoveValid(grid, move):
    valid = True
    # 1st condition: no tile to move
    if (grid[move[0]][move[1]] == 0):
        valid = False
    # 2nd condition: diagonal move
    if (move[0] != move[2] and move[1] != move[3]):
        valid = False
    # 3rd condition: move is more than one space
    if (abs(move[2] - move[0]) > 1 or abs(move[3] - move[1]) > 1):
        valid = False
    # 4th condition: start or end is off the board
    if (move[0] > len(grid) or move[0] < 0 or move[2] > len(grid) or move[2] < 0
            or move[1] > len(grid[1]) or move[1] < 0 or move[3] > len(grid[1]) or move[3] < 0):
        passvalid = False
    return valid


# ***********MAKES MOVES***********
# input: a 2D array representing the grid and the move as an array with 4 integers: [initCol, initRow, newCol, newRow]
# output: if move is valid, return grid with moves made. if move is invalid, return "move is invalid"
def makeMoves(grid, move):
    if (isMoveValid(grid, move)): # only makes move if move is valid
        # swaps the values in the two specified locations
        origValue = grid[move[0]][move[1]]
        newValue = grid[move[2]][move[3]]
        grid[move[0]][move[1]] = newValue
        grid[move[2]][move[3]] = origValue
        return grid
    else:
        return "Move is invalid."


# ***********FORMATS AND outFile.writeS THE GRID***********
# input: a 2D array representing the grid
# output: none; outFile.writes the grid in the designated format
def outFilePrint(grid):
    string = "" # this string represents the grid
    for i in range(0, len(grid)):
        string += "  "
        for j in range(0, len(grid[0])):
          string += str(grid[len(grid) - 1 - i][j]) # accounts for the rows being in reverse order
        string += "\n"
    outFile.write(string)


# called in the main for loop
def runMoves(grid, move):
    grid = makeMoves(grid, move)
    outFilePrint(grid)
    outFile.write("\n")

    while dropCheck(grid) != 0 or len(checkForHorizontalElims(grid, tileEliminationSize)) != 0 or len(checkForVerticalElims(grid, tileEliminationSize)) != 0:
        if (dropCheck(grid) == 0):
            outFile.write("  No drops.")
        else:
            grid = dropping(grid)
            outFile.write("  Board after drops:")
            outFilePrint(grid)
            outFile.write("\n")

        if (len(checkForHorizontalElims(grid, tileEliminationSize)) == 0 and len(checkForVerticalElims(grid, tileEliminationSize)) == 0):
            outFile.write("  No eliminations.")
        else:
            grid = makeHorizontalElims(grid, checkForHorizontalElims(grid,tileEliminationSize))
            grid = makeVerticalElims(grid,  checkForVerticalElims(grid,tileEliminationSize))
            outFile.write("  Board after eliminations:")
            outFilePrint(grid)
        outFile.write("\n")
    if (checkBoardClear(grid)):
        if (len(moves) != movesMade):
            outFile.write(" The board is cleared!\n Skipping " + str(len(moves) - movesMade) + "move(s).")
    return grid


file  = open("input.txt", "r")
datasets = int(file.readline())

outFile = open("output.txt", "w")

outFile.write("Analyzing " + str(datasets) + " data set(s)")

for i in range(0, datasets):
    # initializing vars
    input = readInData()
    tileEliminationSize = int(input[0])
    grid = input[1]
    moves = input[2] #list of moves
    movesMade = 0; # counter variable

    outFile.write("Data Set " + str(i + 1))
    outFile.write("Board Position: \n")
    outFilePrint(grid)
    outFile.write("\n")

    outFile.write(" After move " + str(movesMade) + "\n")
    while dropCheck(grid) != 0 or len(checkForHorizontalElims(grid, tileEliminationSize)) != 0 or len(checkForVerticalElims(grid, tileEliminationSize)) != 0:
        if (dropCheck(grid) == 0):
            outFile.write("  No drops.")
        else:
            grid = dropping(grid)
            outFile.write("  Board after drops:")
            outFilePrint(grid)
            outFile.write("\n")

        if (len(checkForHorizontalElims(grid, tileEliminationSize)) == 0 and len(checkForVerticalElims(grid, tileEliminationSize)) == 0):
            outFile.write("  No eliminations.")
        else:
            grid = makeHorizontalElims(grid, checkForHorizontalElims(grid,tileEliminationSize))
            grid = makeVerticalElims(grid,  checkForVerticalElims(grid,tileEliminationSize))
            outFile.write("  Board after eliminations:")
            outFilePrint(grid)
            outFile.write("\n")
    if (checkBoardClear(grid)):
        if (len(moves) != movesMade):
            outFile.write(" The board is cleared!\n Skipping " + str(len(moves) - movesMade) + "move(s).")

    for i in range(0,len(moves)):
        movesMade += 1
        outFile.write(" After move " + str(movesMade) + "\n")
        grid = runMoves(grid, moves[i])
