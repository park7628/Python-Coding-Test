A, B, N = map(int, input().split())

if ((N-A)/(A-B) + 1) % 1 == 0:
    day = int((N-A)/(A-B) + 1)
else:
    day = int((N-A)/(A-B) + 1) + 1

    
print(day)