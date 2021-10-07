# import sys
# sys.stdin = open("../input.txt", "r")
#
#
# N, M, V = map(int, input().split())
#
# print(N, M, V)
#
# graph = {}
#
# for i in range(M):
#     start, end = map(int, input().split())
#     if start not in graph:
#         graph[start] = list([end])
#     else :
#         graph[start].append(end)
#
# print(graph)
#
# from collections import deque
#
# def BFS(graph, startNode) :
#     visited = list()
#     queue = deque([startNode])
#
#     while(queue) :
#         n = queue.popleft()
#
#         if n not in visited:
#             queue.extend(graph[n])
#             visited.append(n)
#
#     return visited
#
# def DFS(graph, startNode):
#     visited = list()
#     stack = list([startNode])
#
#     while(stack):
#         n = stack.pop()
#         if n not in visited:
#             stack.extend(graph[n])
#             visited.append(n)
#
#     return visited
#
# print(BFS(graph, V))
# print(DFS(graph, V))
#
