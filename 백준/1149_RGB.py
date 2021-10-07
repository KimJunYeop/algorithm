import sys
sys.stdin = open("../input.txt", "r")

N = int(input())
INF = 10000010
result = [INF] * N

print(result)

for i in range(N):
    R,G,B = map(int, input().split())


#     마지막 집을 R, G, B로 칠했을때의 최소값일 수 있지
# **R
# **G
# **B

# 그러면 앞의 값은,, 