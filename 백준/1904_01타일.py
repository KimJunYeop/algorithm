import sys
sys.stdin = open("../input.txt", "r")

# 00 타일들은 모두 붙어있다
# 주어진 n 타일에 대해서 가능한 모든 경우의 수를 구하라
# 순서가 정해진 타일에 대한 순서가 맞춰진 팩토리얼?

# ---- 1   ----- 00
# 위 두가지 경우의 수밖에 없으므로
# d[i] = d[i-1] + d[i-2]

d = [0] * 1000001
n = int(input())

d[1] = 1
d[2] = 2
for i in range(3, n+1):
    d[i] = (d[i-2] + d[i-1]) % 15746

print(d[n])