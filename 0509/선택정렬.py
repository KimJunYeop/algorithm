array = [7,5,9,0,3,1,6,2,4,8]


# 가장 최소값을 찾아서 자리를 바꾼다?

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        # 여기서 최소값을 찾아야지 무슨..
        if array[ ] > array[j]:
            min_index = j
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp

print(array)