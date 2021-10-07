import sys
sys.stdin = open("../input.txt", "r")

N,M = map(int, input().split(' '))
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 방문했으면 0으로 처리하면되서 visited는 필요업서요.

def printMap() :
    print('-------------------\n')
    for i in range(N):
        print(graph[i], end='\n')
    print('-------------------\n')
# 괴물이 0
# 이동가능이 1

dx = [0,1,0,-1]
dy = [-1,0,1,0]

from collections import deque
def bfs(y, x):
    queue = deque()
    queue.append((y,x))
    graph[y][x] = 0
    while queue:
        cur = queue.popleft()
        for i in range(4):
            nx = cur[1] + dx[i]
            ny = cur[0] + dy[i]
            if nx <= -1 or nx >= M or ny <= -1 or ny >= N:
                continue
            print('ny : ',ny,' nx :', nx)
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[cur[0]][cur[1]] + 1
                queue.append((ny,nx))
bfs(0,0)
print(graph[N-1][M-1] + 1)
