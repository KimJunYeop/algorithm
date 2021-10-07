import sys
import heapq

sys.stdin = open("../input.txt", "r")
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    # 두 정점 사이에 여러 개의 간선이 존재할 수 있다.
    # 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.


def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while (q):
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else :
        print(distance[i])



