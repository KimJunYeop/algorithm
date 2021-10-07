import sys
sys.stdin = open("../input.txt", "r")

N, M = map(int, input().split(' '))

# N 행
# M 열
numList = []
print(N,M)
for i in range(N):
    innerList = list(map(int, input().split(' ')))
    numList.append(innerList)

print(numList)
resultList = []
for i in range(N):
    resultList.append(min(numList[i]))

print(max(resultList))