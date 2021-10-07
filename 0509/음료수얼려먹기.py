import sys
sys.stdin = open("../input.txt", "r")
# 생성된 아이스크림의 총 개수를 구하면 된다.
# BFS로 count를 주면서 길을 구한다.


graph = []

for i in range(4):
    graph.append(list(map(int, input())))

print(graph)


def dfs(x,y):
    if x <= -1 or x >= 4 or y <= -1 or y >= 4:
        return False

    if (graph[y][x] == 0):
        graph[y][x] = 1
        dfs(y-1,x)
        dfs(y+1, x)
        dfs(y, x+1)
        dfs(y, x-1)
        return True
    return False

result = 0

for i in range(4):
    for j in range(5):
        if dfs(i,j) == True:
            result += 1

print(result)