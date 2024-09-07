#문제8 백준 1253
n = int(input())
A = list(map(int, input().split()))
A.sort()

end_num = A[n-1]
start_index = 0
end_index = len(A)-2
print(end_index)
count = 0
sum = 0
m = 1

while start_index != end_index:
    sum = A[start_index] + A[end_index]

    if sum == end_num:
        #end_num = end_index
        count+=1
        # print("start =", start_index, "end =", end_index, "count =", count, "end_num =", end_num)
        m+=1
        end_num = A[n-m]
        end_index = len(A) - m -1
        start_index = 0
    elif sum > end_num:
        end_index -=1
    elif sum < end_num:
        start_index += 1

    # if A[start_index] == A[end_index]:
    #     print("들어옴")
    #     m+=1
    #     end_num = A[n-m]
    #     end_index = len(A) - m -1
    #     start_index = 0

print(count)
    
