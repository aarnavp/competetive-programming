t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
 
    if k == 4:
        poss1 = 11
        poss2 = 11
        for x in range(2):
            z = []
            for y in range(n):
                
                if x==0:
                    #print(z)
                    if len(z)>1:
                        if a[y]%2 == 0:
                            if z[0]>z[1]:
                                z[0] = 0
                            else:
                                z[1] = 0
                        
                        elif z[0] - 2-a[y]%2 > 0 and z[0] - 2-a[y]%2 > z[1] - 2-a[y]%2:
                            z[0] = 2-a[y]%2
                        elif z[1] - 2-a[y]%2 > 0 and z[1] - 2-a[y]%2 > z[0] - 2-a[y]%2 :
                            z[1] = 2-a[y]%2
                    else:
                        if a[y]%2 == 0:
                            z.append(0)
                        else:
                            z.append(1)
                if x==1:
                    if a[y]%k == 0:
                        poss2 = 0
                    elif k-a[y]%k<poss2:
                        poss2 = k-a[y]%k
                        
            if len(z)>1:
                z = sorted(z)
                poss1=z[0]+z[1]
        print(min(poss1,poss2))
    else:
        poss = 11
        for x in range(n):
            if a[x]%k == 0:
                poss = 0
            elif k-a[x]%k<poss:
                poss = k-a[x]%k
        print(poss)
