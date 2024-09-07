# # 문제 9 백준 12891 답은 나오나 시간초과
# S, P = map(int, input().split())
# string = input()
# A = ['A', 'C', 'G', 'T']
# ACGT = list(map(int, input().split()))
#
# start_index = 0
# last_index = start_index+P
# end_index = S-1
# count = 0
#
# while last_index < S+1:
#     find_A = 0
#     find_C = 0
#     find_G = 0
#     find_T = 0
#     check_A = string[start_index:last_index]
#     # print(check_A)
#
#     find_A = check_A.count('A')
#     find_C = check_A.count('C')
#     find_G = check_A.count('G')
#     find_T = check_A.count('T')
#     # print('A =',find_A, 'C =', find_C, 'G =',find_G, 'T =', find_T)
#
#     if ACGT[0] <= find_A and ACGT[1] <= find_C and ACGT[2] <= find_G and ACGT[3] <= find_T:
#         count += 1
#         # print("count 증가")
#
#     start_index += 1
#     last_index += 1
#
# print(count)

#다시 풀이

def checkAdd(c):
    if c == "A":
        find_Str[0] += 1
    elif c == "C":
        find_Str[1] += 1
    elif c == "G":
        find_Str[2] += 1
    elif c == "T":
        find_Str[3] += 1

def checkRemove(c):
    if c == "A" and find_Str[0] != 0:
        find_Str[0] -= 1
    elif c == "C" and find_Str[1] != 0:
        find_Str[1] -= 1
    elif c == "G" and find_Str[2] != 0:
        find_Str[2] -= 1
    elif c == "T" and find_Str[3] != 0:
        find_Str[3] -= 1

S, P = map(int, input().split())
string = input()
A = ['A', 'C', 'G', 'T']
ACGT = list(map(int, input().split())) # 각 요소 기준값
find_Str = [0] * 4

start_index = 0
last_index = start_index+P
end_index = S-1
count = 0

for i in range(P):
    checkAdd(string[i])
print(find_Str)

while last_index < S:

    check_A = string[start_index:last_index]
    # print(check_A)

    if ACGT[0] <= find_Str[0] and ACGT[1] <= find_Str[1] and ACGT[2] <= find_Str[2] and ACGT[3] <= find_Str[3]:
        count += 1

    checkAdd(string[last_index])
    checkRemove(string[start_index])
    start_index += 1
    last_index += 1

print(count)



