def eight(n):
    L = []
    while n > 0:
        if (n / 8) > 0:
            L.append(n%8)
            n = n//8
    s = 10**(len(L)-1)
    resert = 0
    L.reverse()
    
    for i in L:
        resert += i * s
        s = s // 10
    return resert

def sixteen(n):
    a = ['A', 'B', 'C', 'D', 'E', 'F']
    string = ''
    while n > 0:
        if ((n%16) < 10):
            string += str(n%16)
            n = n//16
        else:
            string += str(a[(n%16)-10])
            n = n//16
        
        # reversed_string = "".join(reversed(string)) 
        reversed_string = string[ : : -1]
    return reversed_string

n = int(input())

print(eight(n), sixteen(n))
