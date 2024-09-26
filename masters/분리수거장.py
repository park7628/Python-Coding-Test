n = int(input())  # 아파트 단지 수 입력
apart = []   # 아파트 위치와 거주 인구를 저장할 리스트
check = []

# 아파트 위치와 거주 인구 입력 받기
for i in range(n):
    x, y = map(int, input().split())  # x: 아파트 위치, y: 아파트에 거주하는 사람 수
    apart.append((x, y))         # (위치, 거주 인구) 쌍으로 리스트에 추가
    check.append(y)
# 아파트 위치를 기준으로 정렬 (번호가 작은 아파트를 먼저 고려해야 하므로 위치를 기준으로 정렬)
apart.sort()
print(apart)
# 전체 인구의 절반을 넘는 순간을 찾기 위한 준비
peple = sum(a[1] for a in apart)  # 전체 거주 인구의 합
count = 0  # 누적 인구

# 아파트 단지를 순차적으로 보면서 중앙값에 해당하는 단지 찾기
for i in range(n):
    count += apart[i][1]  # 현재 아파트까지의 누적 인구 수 계산
    if count >= peple / 2:  # 누적 인구가 절반을 넘으면 해당 아파트가 중앙값
        print(check.index(apart[i][1]) + 1)  # 아파트 단지는 1번부터 시작하므로 i+1을 출력
        break
# n = int(input())  
# apart = [] 

# for i in range(n):
#     x, y = map(int, input().split()) 
#     apart.append((x, y))         

# apart.sort()

# peple = sum(a[1] for a in apart)  
# for i in range(n):
    
#     if len(apart[][:i]) > len(A[i:]):
        
#         if (A[check_index] > sum(A[check_index+1 :])):
#             print(check_index+1)
#             break
#     elif (A[check_index] > sum(A[:check_index])):
#         print(check_index+1)
#         break