import sys
sys.stdin = open('../input.txt', 'rt', encoding='UTF8')

n = int(input())
product_list = list(map(int, input().split(' ')))
product_list.sort()
m = int(input())
search_list = list(map(int, input().split(' ')))


def binary_search(arr, target, start, end):
    if start > end:
        return "No"

    mid = (start+end) // 2

    if arr[mid] == target:
        return "Yes"
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

for i in range(m):
    print(binary_search(product_list, search_list[i], 0, n-1))