
pay = int(input())
count = 0
coupon = [10, 50, 100, 500, 1000, 5000, 10000, 50000]

for i in range(len(coupon)-1, -1, -1):
    if ((pay // coupon[i]) > 0):
        count += (pay // coupon[i])
        pay = (pay % coupon[i])
        
print(count)