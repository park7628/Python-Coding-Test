n, target = map(int, input().split())
L = list(map(int, input().split()))

try:
    print(L.index(target)+1)
except:
    print(-1)