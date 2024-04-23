# 문제8 백준 1253을 변형한 문제(교재로 치면 맞음) / (백준에서는 틀림)
n = int(input())
A = list(map(int, input().split()))
A.sort()

end_num = A[n - 1]
start_index = 0
end_index = len(A) - 2
count = 0
sum = 0

while len(A) != 1:


    if start_index == end_index:
        break

    sum = A[start_index] + A[end_index]

    if sum == end_num:
        count += 1
        A.pop()
        start_index = 0
        end_index = len(A) - 1
        end_num = len(A)
    elif sum > end_num:
        end_index -= 1
    elif sum < end_num:
        start_index += 1

print(count)

