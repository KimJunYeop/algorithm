import sys
sys.stdin = open("../input.txt", "r")

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))



arr.reverse()
result = 0
for num in arr:
    mok = m // num
    result += mok
    m -= num * mok

print(result)