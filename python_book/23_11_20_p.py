
'''
L = []
for i in range(6):
    #a = list(map(int, input().split()))
    a = input()
    a = int(a)
    L.append(a)
    
print(L)
L = list(set(L))
print(L)

for j in range(len(L)):
    print(L[j], end="\n")
'''

import random

testcase = int(input())
answer = 0
A = [0] * (100001)

for i in range(0, 100001):
    A[i] = random.randrange(1, 101)

print(A)
for t in range(1, testcase+1):
    start, end = map(int, input().split())

    for i in range(start, end+1):
        answer += A[i]


    print(str(t) +" "+ str(answer%2))
    answer = 0
