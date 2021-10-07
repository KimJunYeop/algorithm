import sys
sys.stdin = open("../input.txt", "r")

INF = int(1e9)
# n은 간선의 갯수
# m은 경로의 갯수
n,m = map(int, input().split())

graph = [[] for i in range(n+1)]
print(graph)
visited = [False] * (n+1)
distance = [INF] * (n+1)

start = int(input())

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

# graph의 [0] 목적지
# graph의 [1] 목적지까지의 distance
def find_min_index():
#     distance 중 최소 경로가 가장 작은 distance를 반환한다.
    min_index = INF
    min_value = INF
    for i in range(n+1) :
        if min_value > distance[i] and not visited[i]:
            min_value = distance[i]
            min_index = i

    return min_index

print(graph)
def diajstra(start):
    visited[start] = True
    distance[start] = 0
    for j in graph[start]:
        distance[j[0]] = j[1]
    print(distance)

#   이제 최소경로를 찾아야지.
    for i in range(n-1) :
        min_index = find_min_index()
        visited[min_index] = True
        for j in graph[min_index]:
            cost = distance[min_index] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


diajstra(start)
print(distance)