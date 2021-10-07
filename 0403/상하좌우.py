import sys
sys.stdin = open("../input.txt", "r")

N = int(input())
commandList = list(input().split(" "))

print(N, commandList)

direction = ['U','R','D','L']
dx = [0,1,0,-1]
dy = [-1,0,1,0]

curPos = [1,1]

for i in commandList:
    for j in range(4):
        if i == direction[j]:
            newPosY = curPos[0] + dy[j]
            newPosX = curPos[1] + dx[j]

    if(newPosY < 1 or newPosX < 1 or newPosX > N or newPosY > N):
        continue
    curPos = [newPosY, newPosX]

print(curPos)
