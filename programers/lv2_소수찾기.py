from itertools import permutations
def prime_check(i): #소수 판별을 함수화 / return하여 bool 값을 저장
    if (i == 1) or (i == 0):
        return False
    elif i == 2:
        return True
    else:
        for j in range(2, i):
            if (i % j == 0):
                return False
    return True

def solution(numbers):
    L = list(numbers)
    per = []
    answer=0
    for i in range(1,len(L)+1):
        per += list(map(''.join,permutations(L,i))) 
        
    per = sorted(set(map(int, per))) # int형 변형, 중복제거, 정렬을 한줄로 처리(계산 시간이 소폭 줄어듬)
    
    for i in per:
        if prime_check(i) == True:
            answer+=1
    return answer