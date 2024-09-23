'''n = int(input())
L = []
for i in range(n):
    L.append(list(input().split()))
    
    
dict_L = dict(L)
print('dict_L', dict_L)
sorted_dict = sorted(dict_L.items(), key = lambda a : a[1] , reverse = True)
print('sorted_dict', sorted_dict)

for i in range(3):
    print(list(sorted_dict[i])[0])
    '''
    
n = int(input())
L = []
name = []
iq = []
for i in range(n):
    a, b = input().split()
    name.append(a)
    iq.append(int(b))

for i in range(3):
    max_index = iq.index(max(iq))
    print(name[max_index])
    name.pop(max_index)
    iq.pop(max_index)
    
    
