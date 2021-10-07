import sys

sys.stdin = open("../input.txt", "r")


N, M = map(int, input().split(' '))

graph = []


for i in range(N):
    graph.append(list(map(int, input())))

from collections import deque

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs(x, y) :
    queue = deque()
    queue.append([y,x])

    while queue:
        newy, newx = queue.popleft()
        for i in range(4):
            nx = newx + dx[i]
            ny = newy + dy[i]

            if nx <= -1 or nx >= M or ny <= -1 or ny >= N :
                continue

            if (graph[ny][nx] == 1) :
#                 미방문일경우.
                graph[ny][nx] = graph[newy][newx] + 1
                queue.append([ny, nx])


bfs(0,0)
for i in range(N):
    print(graph[i])

print(graph[N-1][M-1])


