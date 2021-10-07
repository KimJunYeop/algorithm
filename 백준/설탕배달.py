import sys
sys.stdin = open("../input.txt", "r")

n = int(input())
count = 0
result = []

while(1):
    # n1을 최대까지?
    n1 = n // 5 - count
    n2 = (n - 5 * n1) // 3

    if n1 < 0:
        print(-1)
        break;

    if n1 * 5 + n2 * 3 == n:
        print(n1+n2)
        break
    else :
        count += 1

