file=open("C:\Users\Elizabeth\Programming\Rowan\input.txt", "r+")
inputData=file.readlines()
dataSets=inputData[0]
dimensions=inputData[1].split(" ")
intDimensions= [int(dimensions[0]), int(dimensions[1])]
i=2
table=[]
for i in range(2, intDimensions[1]+2):
    table.append(inputData[i].split(" "))
j=0
h=0
for x in table:
    for j, y in enumerate(x):
        x[j] = y.strip()
robotStart=inputData[6].split(" ")
intRobotStart= [int(robotStart[0]), int(robotStart[1])]
seventhLine = inputData[7].split(" ")
strength=int(seventhLine[0])
agility=int(seventhLine[1])
instructions=int(inputData[8])
commands=inputData[9].split(" ")
file.close()
if(intRobotStart[0]>intDimensions[0] or intRobotStart[1]>intDimensions[1]):
    print("Input Invalid")

if(table[int(intRobotStart[1])][int(intRobotStart[0])]>0):
    table[int(intRobotStart[1])][int(intRobotStart[0])] = 0

#if(table<0): #and abs(table[int(intRobotStart[1])][int(intRobotStart[0])])>agility):
 #   print("Robot fell in the hole")

print 'Analyzing: ',dataSets, 'data set(s)'
print "Robot Start: ", intRobotStart[0], " ", intRobotStart[1]
print "Robot Strength and Agility: ", strength, agility
print "Instructions: ", instructions
print "Table Configuration:"
for i in range(0, intDimensions[1]):
    print table[i]

#28517F, M52089
    