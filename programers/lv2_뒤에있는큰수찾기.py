def solution(numbers):
    n = len(numbers)
    answer = [-1] * n  # 정답을 -1로 초기화
    stack = []  # 스택을 초기화

    for i in range(n - 1, -1, -1):  # 배열을 오른쪽에서 왼쪽으로 순회
        # 현재 숫자보다 작은 숫자는 스택에서 제거
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        
        # 스택이 비어 있지 않다면 스택의 맨 위가 '뒤에 있는 큰 수'
        if stack:
            answer[i] = stack[-1]
        
        # 현재 숫자를 스택에 추가
        stack.append(numbers[i])

    return answer