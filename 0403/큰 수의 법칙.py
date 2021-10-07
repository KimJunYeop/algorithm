import sys
sys.stdin = open("../input.txt", "r")

N, M, K = map(int, input().split(' '))

numList = list(map(int, input().split(' ')))
numList.sort()

first = numList[N-1]
second = numList[N-2]

result = 0

while True:
    for i in range(K):
        if M == 0 :
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)