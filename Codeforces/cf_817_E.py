T = int(input())
for _ in range(T):
    N, Q = map(int, input().split())
    precomp = [[0 for _ in range(1000)] for _ in range(1000)]
    for _ in range(N):
        h, w = map(int, input().split())
        precomp[h-1][w-1] += (h)*(w)
 
    #evaluate precomp array
 
    for x in range(1000):
        for y in range(1000):
            if x>0 and y>0:
                precomp[x][y] += precomp[x-1][y] + precomp[x][y-1] - precomp[x-1][y-1]
            elif x>0:
                precomp[x][y] += precomp[x-1][y]
            elif y>0:
                precomp[x][y] += precomp[x][y-1]
 
    for _ in range(Q):
        hs, ws, hb, wb = map(int, input().split())
        res = precomp[hb-2][wb-2]-(precomp[hs-1][wb-3]+precomp[hb-3][ws-1])+precomp[hs-1][ws-1]
        print(res)
                
                
