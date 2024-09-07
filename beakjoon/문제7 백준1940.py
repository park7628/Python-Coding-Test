# 답이랑은 다르지만 풀이 성공 백준 1940
n = int(input())
num = int(input())
A = list(map(int, input().split()))

A.sort()

end_index = len(A) -1
start_index = 0
sum = 1
count = 0
while start_index != end_index:
    sum = A[start_index] + A[end_index]
    if sum == num:
        count+=1
        end_index-=1
    elif sum < num:
        start_index+=1
    elif sum > num:
        end_index-=1

print(count)

