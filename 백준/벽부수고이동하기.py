import sys
sys.stdin = open("../input.txt", "r")

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input())))

def printArr(arr):
    print("---------------")
    for i in range(N):
        for j in range(M):
            print("{:3d}".format(arr[i][j]), end=' ')
        print()


from collections import deque
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 이제 여기서 한칸을 부실수 있다.
# 하나씩 다 부셔버리면 되겠구만?
result = []
INF = int(1e9)
def bfs(startY, startX, arr):
    global INF
    queue = deque([[startY,startX]])
    visited = [[0]*M for _ in range(N)]
    visited[startY][startX] = 0
    arr[startY][startX] = 1

    while(queue):
        now = queue.popleft()
        nowY = now[0]
        nowX = now[1]

        for i in range(4):
            newY = nowY + dy[i]
            newX = nowX + dx[i]
            if newY < 0 or newY >= N or newX < 0 or newX >= M:
                continue
            if visited[newY][newX] == 0 and arr[newY][newX] == 0:
                queue.append([newY,newX])
                visited[newY][newX] = 1
                arr[newY][newX] = arr[nowY][nowX] + 1

    if arr[N-1][M-1] == 0:
        result.append(INF)
    else :
        result.append(arr[N-1][M-1])

def copyMap(arr1, arr2):
    for i in range(N):
        for j in range(M):
            arr1[i][j] = arr2[i][j]

copyarr = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            copyMap(copyarr, arr)
            arr[i][j] = 0
            bfs(0,0,arr)
            arr[i][j] = 1
            copyMap(arr, copyarr)

minValue = min(result)
if(minValue == INF):
    print(-1)
else :
    print(minValue)