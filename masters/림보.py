n = int(input())
rimbo = list(map(int, input().split()))
pass_check = True

for i in rimbo:
    if (i <= 160):
        print('I', i)
        pass_check = False
        break
    
if (pass_check == True):
    print('P')