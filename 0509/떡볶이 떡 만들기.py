import sys
sys.stdin = open('../input.txt', 'rt', encoding='UTF8')

n, target = map(int, input().split(' '))
print(n, target)

arr = list(map(int, input().split(' ')))
arr.sort()
print(arr)

def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end)//2

    customResult=0
    print('start :', start, ' end : ', end , ' mid : ',mid)
    for i in arr:
        if i-mid > 0:
            customResult += (i - mid)
    print(customResult)
    # 떡의 길이가 딱 맞는게 최대값이 맞다
    if customResult == target:
        return mid
    elif customResult < target:
        # customResult가 target 값 보다 작으면 더 적게 잘라야지 많이 나오지.
        return binary_search(arr, target, start, mid-1)
    else :
        return binary_search(arr, target, mid + 1, end)

    # custom_result =
    # start = min
    # end = max
print(binary_search(arr, target, arr[0], arr[n-1]))

