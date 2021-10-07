
d = [0] * 10010
d[0] = 1
d[1] = 1

n = 10
for x in range(3, n+1):
    d[x] = d[x-1] + d[x-2]

print(d[10])