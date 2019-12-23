#Define Substantive Functions
def printGrid(grid):
    for row in grid:
        rowString = ""
        for char in row:
            if int(char) >= 0:
                rowString += char + "  "
            else:
                rowString += char + " "
        print "    " + rowString

def dir2DeltaCoordinate(direction):
    if(direction == "E"):
        return [1, 0]
    elif(direction == "W"):
        return [-1, 0]
    elif(direction == "N"):
        return [0, -1]
    elif(direction == "S"):
        return [0, 1]

def getLocationHeight(grid, currentX, currentY, direction):
    delta_coordinate = dir2DeltaCoordinate(direction)
    return grid[currentY + delta_coordinate[1]][currentX + delta_coordinate[0]]

#This is the main function that solves the problem
def solve(grid, directions, strength, agility, initialX, initialY):

    initial_location_height = grid[initialY][initialX]

    #checks if the robot is off the table
    if(initialX > len(grid[0]) or initialY > len(grid) or initialX < 0 or initialY < 0):
        return "Robot is off the table."

    #checks if the initial location is too shallow for the robot to move out
    if(initial_location_height < 0 and abs(int(initial_location_height)) < int(agility)):
            return "Robot is fell in a hole and it's not agile enough to get out."

    #at this point, the robot should be safe
    print("Robot deployed successfully")

    #makes the initial location value 0 if it's initially positive
    if(initial_location_height > 0):
        grid[initialY][initialX] = 0 #makes the starting location 0

    currentX = initialX
    currentY = initialY
    for direction in directions:
        current
        deltaCoordinate = dir2DeltaCoordinate(direction)
        print(direction)
        print("[" + str(currentX) + ", " + str(currentY) + "]")
        print(deltaCoordinate)
        newLocation = [currentY + deltaCoordinate[0], currentX + deltaCoordinate[1]]
        print(newLocation)

        if(newLocation[0] > len(grid[0]) or newLocation[1] > len(grid) or newLocation[0] < 0 or newLocation[1] < 0):
            return "The robot fell off the grid"

        height = getLocationHeight(grid, currentX, currentY, direction)


        if(height == 0):
            currentX += newLocation[0]
            currentY += newLocation[1]
        elif(height > 0):
            if(height == strength):
                grid[newLocation[1]][newLocation[0]] = 0
                currentX += newLocation[0]
                currentY += newLocation[1]
            elif(height > strength):
                grid[newLocation[1]][newLocation[0]] -= strength
            else:
                currentX += newLocation[0]
                currentY += newLocation[1]
        else:
            if(abs(height) > agility):
                print "Not agile enough, the robot doesn't move"
            else:
                currentX += newLocation[0]
                currentY += newLocation[1]

    print(str(len(directions)) + " Instructions Processed; Robot at (" + str(currentX) + ", " + str(currentY) + ")")
    print("+-- Table Configuration:")
    printGrid(grid)


file  = open("sample1.txt", "r")
datasets = int(file.readline())

print("Analyzing " + str(datasets) + " data set(s)")

for i in range(0, datasets):
    print("Data Set " + str(i+1))

    dimensions = file.readline().split()

    grid = []
    for j in range(0, int(dimensions[1])):
        grid.append(file.readline().split())

    startingLocation = file.readline().split()
    initialX = int(startingLocation[0])
    initialY = int(startingLocation[1])
    print("+-- Robot Start: " + str(initialX) + " " + str(initialY))

    ability = file.readline().split()
    strength = ability[0]
    agility = ability[1]
    print("+-- Robot Strength and Ability: " + str(strength) + " " + str(agility))

    instructionCount = int(file.readline())
    print("+-- Instructions: " + str(instructionCount))

    directions = file.readline().split()
    print("+-- Initial Table Configuration:")
    printGrid(grid)
    #Parse File using file.readline()
    #Call Substantive Functions
    print(solve(grid, directions, strength, agility, initialX, initialY))
