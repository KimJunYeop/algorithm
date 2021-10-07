import sys
sys.stdin = open("../input.txt", "r")

N,M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))



def dfs(y, x):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False

    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(y+1,x)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y, x-1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1

print(result)