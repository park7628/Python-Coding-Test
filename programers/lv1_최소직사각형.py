# def solution(sizes):
#     firstMax = [] #리스트 안에 있는 것 중 큰것
#     secondMax = [] #리스트 안에 있는 것 중 작은것
#     answer = 0
#     # print(len(sizes))
#     for i in range(len(sizes)):
#         if (sizes[i][0] >= sizes[i][1]):
#             firstMax.append(sizes[i][0])
#             secondMax.append(sizes[i][1])
#         else:
#             firstMax.append(sizes[i][1])
#             secondMax.append(sizes[i][0])
#     answer = max(firstMax) * max(secondMax)
    
#     return answer

# 

def solution(sizes):
    print(max(x) for x in sizes)
    return (max(i if i>= j  else j for i, j in sizes ) * max(i if i<= j  else j for i, j in sizes ))

L = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(L))

#명함을 돌리는게 가능함으로 가장 긴 면을 찾는게 1차적인 목표라고 생각했다.
#명함의 가로든 세로든 큰값중에 가장 큰값, 작은값 중에 가장 큰값을 찾아 곱해주면 해결된다고 생각했다.
#그러나 코드가 효율적이지 못하다 생각했다.(range가 시간을 많이 잡아먹음 / 간략하게 표현 가능)
# print(L)
