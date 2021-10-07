import sys
sys.stdin = open('../input.txt', 'rt', encoding='UTF8')

N, K = map(int, input().split(' '))
print(N, K)

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

print(a)
print(b)

a.sort()
b = sorted(b, reverse=True)

print(a)
print(b)

# 이제 K만큼 a와 b를 비교해서 바꿔치기하면된다?

for i in range(K):
    if(a[i] < b[i]):
        a[i], b[i] = b[i], a[i]

print(a)
print(b)

print(sum(a))
