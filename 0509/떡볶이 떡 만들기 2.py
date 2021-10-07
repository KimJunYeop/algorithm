import sys
sys.stdin = open('../input.txt', 'rt', encoding='UTF8')


n, target = map(int, input().split(' '))
print(n, target)

arr = list(map(int, input().split(' ')))
arr.sort()
print(arr)

start = 0
end = max(arr)

result = 0
while(start <= end):
    total = 0
    mid = (start + end)//2
    for x in arr:
        if x > mid:
            total += x-mid

    if total < target:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)