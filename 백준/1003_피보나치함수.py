import sys
sys.stdin = open("../input.txt", "r")

T = int(input())

# def fibonachi(n) :
#     global zeroCount
#     global oneCount
#     if(n == 0) :
#         zeroCount += 1
#         return 0
#     elif(n == 1) :
#         oneCount += 1
#         return 1
#     else :
#         return fibonachi(n-2) + fibonachi(n-1)

for i in range(T):
    n = int(input())
    f = [0] * 51
    # okay 시간초과
    countList = [[0] * 2 for i in range(50)]
    f[0] = 0
    f[1] = 1
    # 다시 메모리제이션을하면될거같은데요?
    countList[0][0] = 1
    countList[1][1] = 1
    for i in range(2, n+1):
        f[i] = f[i-2] + f[i-1]
        countList[i][0] = countList[i-2][0] + countList[i-1][0]
        countList[i][1] = countList[i-2][1] + countList[i-1][1]

    print(countList[n][0], countList[n][1])

