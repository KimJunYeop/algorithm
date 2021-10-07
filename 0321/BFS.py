# graph_list = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}
#
# graph_test = {
#     'a': set(['b','c','d'])
# }
#
# listTest = list()
# print(graph_test['a'])
# listTest.extend(graph_test['a'])
# print(listTest)
# root_node = 1
#
#
# from collections import deque
#
# def BFS(graph, startNode):
#     visit = list()
#     queue = deque([startNode])
#
#     while(queue) :
#         n = queue.popleft()
#         if n not in visit :
#             queue.extend(graph[n])
#             visit.append(n)
#     return visit
#
# def BFS2(graph, startNode):
#     visited = list()
#     queue = list()
#
#     queue.append(startNode)
#
#     while(queue) :
#         n = queue.pop(0)
#         if n not in visited:
#             visited.append(n)
#             queue.extend(graph[n])
#
#     return visited
#
# def DFS(graph, startNode):
#     visited = list()
#     stack = list()
#
#     stack.append(startNode)
#
#     while(stack) :
#         n = stack.pop()
#         if n not in visited:
#             stack.extend(graph[n])
#             visited.append(n)
#
#     return visited
#
# print(BFS(graph_list, 1))
# print(BFS2(graph_list, 1))
#
# print(DFS(graph_list, 1))