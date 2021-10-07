import sys
sys.stdin = open("../input.txt", "r")

N, K = map(int, input().split(' '))

count = 0


print(N)
print(K)
print(N//K)
print(N%K)

while True:
    if N == 1:
        break

    if N % K == 0:
        # 나누어 떨어진다면
        N = N//K
    else :
        N -= 1
    count += 1

print(count)