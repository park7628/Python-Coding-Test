t1, t2, t3 = map(int, input().split())

if (t1 == 0) or (t2 == 0) or (t3 == 0):
    print('F')
else:
    if sum([t1, t2, t3]) == 180:
        print('P')
    else: 
        print('F')