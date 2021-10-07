import sys
sys.stdin = open('../input.txt', 'rt', encoding='UTF8')

n = int(input())
arr = []
for i in range(n):
    input_data = input().split(' ')
    print(input_data)
    arr.append([input_data[0], int(input_data[1])])

print(arr)

arr = sorted(arr, key=lambda student: student[1])

print(arr)