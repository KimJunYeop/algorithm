import sys
sys.stdin = open("../input.txt", "r")

T = int(input())
d = [0] * 101

#  1, 1, 1, 2, 2, 3, 4, 5, 7, 9
for i in range(T):
    n = int(input())

    d[1] = 1
    d[2] = 1
    d[3] = 1

    for i in range(4, n+1):
        d[i] = d[i-2] + d[i-3]
    print(d[n])