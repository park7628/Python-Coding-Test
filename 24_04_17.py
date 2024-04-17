# 문제 6, 백준 2018 / 메모리 초과
# n = int(input())


# A = []
# for i in range(n):
#     A.append(i+1)
# print(A)

# sum = 0
# count = 0
# for i in range(0,n):
#     sum = 0
#     for j in range(i, n):
#         sum += A[j]
#         if sum == n:
#             count+=1
#             sum = 0
#             break
    
# print(count)

#--------new 실패 메모리초과
# n = int(input())

# A = []
# for i in range(n):
#     A.append(i+1)

# startIndex = 0
# endIndex = 0
# sum = 0
# i=0
# count=0

# while(endIndex != n):
#     sum += A[i]
#     i+=1
#     print("sum =",sum)
    
#     if sum == n:
#         count+=1
#         startIndex += 1
#         endIndex = i
#         i = startIndex
#         sum = 0
#         print("count =",count)

#     elif sum > n:
#         startIndex += 1
#         sum = 0
#         endIndex = i
#         i = startIndex
#     print("endIndex =", endIndex)
    
        

# print(count+1)

#--------답지 투포인터라는 개념을 이해하기
n= int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while (end_index != n):
    
    if sum == n:
        count+=1
        end_index +=1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index +=1
        sum += end_index
print(count)