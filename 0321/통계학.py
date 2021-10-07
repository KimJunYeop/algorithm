# import sys
# sys.stdin = open("../input.txt", "r")
#
# length = int(input())
# numList = []
#
# for i in range(length):
#     numList.append(int(input()))
#
# print(numList)
#
#
# # 산술 평균
# sanSum = 0
# sanAvg = 0
#
# for i in numList:
#     sanSum += i
# sanAvg = round(sanSum / length)
#
#
# # 중앙값
# centerValue = 0
# numList.sort()
#
# if length % 2 == 0 :
#     centerValue = (numList[length//2] + numList[length//2+1])/2
# else :
#     centerValue = numList[length//2]
#
# # 최빈값
# # 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
#
# numCountList = list(0 for i in range(40001))
#
# import collection
#
# print(testList)
#
# for i in numList:
#     numCountList[i] += 1