import sys
sys.stdin = open("../input.txt")

n = int(input())
arr = list(map(int, input().split()))
smallResult = 0
largeResult = 0

if n == 1:
    print(arr[0])
else :
    arr.sort()
    for i in arr:
        smallResult += i
        largeResult += smallResult
    print(largeResult)