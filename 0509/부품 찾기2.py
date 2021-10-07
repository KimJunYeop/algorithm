import sys
sys.stdin = open('../input.txt', 'rt', encoding='UTF8')

n = int(input())
product_list = list(map(int, input().split(' ')))
product_list.sort()
m = int(input())
search_list = list(map(int, input().split(' ')))

a = [0] * 1000100

for i in product_list:
    a[i] = 1

for i in search_list:
    if a[i] == 0:
        print("no")
    else:
        print("yes")
