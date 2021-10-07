# 왜 틀렸는지 확인해야함.

import sys
sys.stdin = open("../input.txt", "r")
N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))


def printMap():
    print('-------------------------\n')
    for i in range(N):
        print(graph[i])
    print('-------------------------\n')


# printMap()
# DFS랑 BFS 둘다로 풀어봅시다.

count = 2
dx = [0,1,0,-1]
dy = [-1,0,1,0]

from collections import deque

def bfs(y, x, count):
    queue = deque()
    queue.append((y,x))
    while(queue) :
        cur = queue.popleft()
        for i in range(4):
            nx = cur[1] + dx[i]
            ny = cur[0] + dy[i]

            if(nx <= -1 or nx >= N or ny <= -1 or ny >= N):
                continue

            if graph[ny][nx] == 1:
                queue.append((ny,nx))
                graph[ny][nx] = count
    count += 1
count = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j, count)
            count += 1

villageCount = count-2
houseList = []
def searchMap(houseNum):
    houseLength = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == houseNum:
                houseLength += 1

    return houseLength

for i in range(2, count):
    houseList.append(searchMap(i))

print(len(houseList))
houseList.sort()
for i in houseList:
    print(i)