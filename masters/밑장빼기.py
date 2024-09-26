n = int(input())
card = list(map(int, input().split()))

check = True
while (len(card) > 0):
    if(card[0] == min(card)):
        card.pop(0)
    elif(card[-1] == min(card)):
        card.pop()
    else:
        check = False
        break
    
if check:
    print('YES')
else:
    print('NO')