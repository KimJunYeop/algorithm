import sys
sys.stdin = open("../input.txt", "r")

N,K = map(int, input().split())

# N + (n+1, n-1, 2*n)
# 세가지 경우의 수가 존재한다.
# 5 4 8 16 17
# 5 10 9 18 17

# DFS로 모든 경우의수를 진행한다?
visited = [0] * 100001
MAX = 100000
from collections import deque
def bfs(start, count, target):
    global MAX
    queue = deque()
    queue.append([start, count])

    while(queue):
        now = queue.popleft()
        nowPos = now[0]
        if nowPos == target :
            return now[1]
        nowCount = now[1] + 1

        if visited[nowPos] == False:
            if nowPos+1 <= MAX :
                queue.append([nowPos + 1, nowCount])
                visited[nowPos] = True
            if nowPos-1 >= 0 :
                queue.append([nowPos - 1, nowCount])
                visited[nowPos] = True
            if nowPos * 2 <= MAX:
                queue.append([nowPos*2, nowCount])
                visited[nowPos] = True
    return count
print(bfs(N,0,K))
