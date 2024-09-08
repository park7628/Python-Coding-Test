'''

def solution(answers):
    answer = []
    case1 = [1, 2, 3, 4, 5]
    case2 = [2, 1, 2, 3, 2, 4, 2, 5]
    case3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    c1, c2, c3 = 0, 0, 0
    
    for i in range(len(answers)):
        
        
        if c1 >= len(case1):
            c1 = 0
            if case1[c1] == answers[i]:
                count[0]+=1
        else:
            if case1[c1] == answers[i]:
                count[0]+=1
                
        # print(c1)
        if c2 >= len(case2):
            c2 = 0
            if case2[c2] == answers[i]:
                count[1]+=1
        else:
            if case2[c2] == answers[i]:
                count[1]+=1
                
                
        if c3 >= len(case3):
            c3 = 0
            if case3[c3] == answers[i]:
                count[2]+=1
        else:
            if case3[c3] == answers[i]:
                count[2]+=1
        c1+=1
        c2+=1
        c3+=1
        # print(f"{i+1}회 완료")
    # print(count)
    
    for k in range(1, 4):
        if count[k-1] == max(count):
            answer.append(k)
    
            
        
    return answer
L = [1, 2, 3, 4, 5, 1, 3, 5, 2, 4]
print(solution(L))

'''

def solution(answers):
    answer = []
    case1 = [1, 2, 3, 4, 5]
    case2 = [2, 1, 2, 3, 2, 4, 2, 5]
    case3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    
    # 답안과 비교하며 각 case의 정답 개수를 셈
    for i in range(len(answers)):
        if case1[i % len(case1)] == answers[i]:
            count[0] += 1
        if case2[i % len(case2)] == answers[i]:
            count[1] += 1
        if case3[i % len(case3)] == answers[i]:
            count[2] += 1
    
    # 가장 많은 정답을 맞춘 사람(들)을 찾기
    max_count = max(count)  # max(count)를 한 번만 계산
    for k in range(1, 4):
        if count[k - 1] == max_count:
            answer.append(k)

    return answer

# 테스트 코드
L = [1, 2, 3, 4, 5, 1, 3, 5, 2, 4]
print(solution(L))
