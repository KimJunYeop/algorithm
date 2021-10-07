import sys
sys.stdin = open("../input.txt", "r")

N, target = map(int, input().split(' '))
inputArr = list(map(int, input().split(' ')))

print(inputArr)

def binary_search(inputArr, target, start, end):
    if(start > end):
        return "hello"

    mid = (start+end)//2

    if(inputArr[mid] == target) :
        return mid
    elif (inputArr[mid] > target):
        return binary_search(inputArr, target, start, mid-1)
    else :
        return binary_search(inputArr, target, mid+1, end)

print(binary_search(inputArr, 7, 0, N-1))