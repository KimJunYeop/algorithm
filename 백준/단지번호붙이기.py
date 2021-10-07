import sys
sys.stdin = open("../input.txt", "r")

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))

print(arr)

def printArr(arr):
    print('----- printArr -----')
    for i in range(N):
        for j in range(N):
            print("{:3d}".format(arr[i][j]), end=' ')
        print()

