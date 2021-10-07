import sys
sys.stdin = open("../input.txt", "r")

M,N = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))


def printArr(arr):
    print('----------------')
    for i in range(N):
        for j in range(M):
            print("{:3d}".format(arr[i][j]), end= ' ')
        print()

from collections import deque

dx = [0,1,0,-1]
dy = [-1,0,1,0]

queue = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i, j])

def bfs():
    while(queue):
        now = queue.popleft()
        nowY = now[0]
        nowX = now[1]

        for i in range(4):
            newY = nowY + dy[i]
            newX = nowX + dx[i]

            if newY < 0 or newX < 0 or newY >= N or newX >= M:
                continue

            if arr[newY][newX] == 0:
                arr[newY][newX] = arr[nowY][nowX]+1
                queue.append([newY, newX])

bfs()
zeroCount = 0
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
          zeroCount += 1
if zeroCount > 0 :
    print(-1)
else:
    print(max(max(arr))-1)