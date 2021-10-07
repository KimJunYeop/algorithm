import sys
sys.stdin = open("../input.txt", "r")

startPos = input()
startPosX = ord(startPos[0]) - ord('a') + 1
startPosY = int(startPos[1])

print(startPosX)
print(startPosY)

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

#
steps = [(-1,2), (1,2), (2,1,), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1)]

count = 0
# 가능한 갯수를 구하면 되는거잖아?
# 8개를 다돌면서 진행하면 되겠죠.

for i in range(8) :
    newPosX = startPosX + steps
    [i][0]
    newPosY = startPosY + steps[i][1]

    if(newPosX < 1 or newPosY < 1 or newPosX > 8 or newPosY > 8):
        continue
    count += 1

print(count)