userID = list(input())
checkID = True
if len(userID) <= 20:
    for i in userID:
        if ((ord(i)>= 65) and (ord(i)<= 90)) or ((ord(i)>= 97) and ord(i)<= 122):
            continue
        else:
            checkID = False
            break
else:
    checkID = False

if checkID == True:
    print('P')
else:
	print('I')