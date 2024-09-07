# n, q = map(int, input().split())
# L = list(map(int, input().split()))
# sumList = []
# sumNum = 0
# for k in range(q):
#     i, j = map(int, input().split())
#     for s in range(i-1, j):
#         sumNum += L[s]
#     sumList.append(sumNum)
#     # print(sumNum)
#     sumNum = 0

# for i in range(len(sumList)):
#     print(sumList[i])
# # 각 자리의 숫자의 합을 먼저 정한다음 리스트로 만들고 i와 j가 주어졌을 때 리스트[j] - 리스트[i-1] 해서 구하기

# xn, yn = map(int, input().split())
# numList = [0 for i in range(xn)]
# for i in range(xn):
#     numList[i] = list(map(int, input().split()))

# print(numList)
# sumNum = 0
# for i in range(yn):
#     x1, y1, x2, y2 = map(int, input().split())
#     for n in range(x1-1, x2):
#         for m in range(y1-1, y2):
#             sumNum += numList[n][m]
#     print(sumNum)
#     sumNum = 0
    







