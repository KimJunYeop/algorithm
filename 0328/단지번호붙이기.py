# import sys
# sys.stdin = open("../input.txt", "r")
#
# N = int(input())
# visit = []
# visit = [[0]*N]*N
#
# graph = []
#
# for i in range(N):
#     graph.append(list(map(int, input())))
#
# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
#
# from collections import deque
#
# def findStartNode():
# #     가장 처음의 1인 startNode를 찾는다.
#     flag = 0
#     startX = 0
#     startY = 0
#     for i in range(N):
#         for j in range(N):
#             if graph[i][j] == 1:
#                 flag = 1
#                 startX = j
#                 startY = i
#                 break
#
#         if flag == 1:
#             break
#     return [startY, startX]
#
# def BFS():
#     # BFS를 진행하면서 1인 지역만 방문하면 해당 지도를 얻을 수 있지 않을까?
#     # cnt를 증가시키면서 얻으면 해당 방법으로 가능할 것 같은데.
#     startNode = findStartNode()
#     queue = deque()
#     queue.append(startNode)
#     visit[startNode[0]][startNode[1]] = 1
#     countMap = [[0]*N]*N
#     cnt = 1
#     while queue:
#         cur = queue.popleft()
#         # cur도 현재 방문한데에 넣어야되지않아?
#         for i in range(4):
#             print('cur :', cur)
#             newPos = [cur[0] + dy[i], cur[1] + dx[i]]
#             print('newPos :', newPos)
#             if 0 <= newPos[0] < N and 0 <= newPos[1] < N:
#                 if graph[newPos[0]][newPos[1]] == 1 & visit[newPos[0]][newPos[1]] == 0:
#                     # 방문가능
#                     visit[newPos[0]][newPos[1]] == 1
#                     queue.append([newPos[0], newPos[1]])
#                     countMap[newPos[0]][newPos[1]] = cnt
#     return countMap
#
# print(BFS())
#
