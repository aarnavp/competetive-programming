import time
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    prefixes = []
    tot = 0
    for _ in range(n):
        pre = [0]
        arr = list(map(int, input().split()))
        for y in range(m):
            pre.append(arr[y]+pre[y])
 
        tot+=pre[m]
        prefixes.append(pre)
 
    og = tot
    
    i = 0
    j = m
    ret = ""
    while True:
        #time.sleep(0.1)
        #print(tot)
        if tot-(prefixes[i][m]-prefixes[i][j]) == og//2:
            
            break
        elif j==0:
            j = m
            tot-=prefixes[i][m]
            ret+="D"
            i+=1
        else:
            j-=1
    ret+="R"*j
    ret+="D"
    ret+="R"*(m-j)
    ret+="D"*(n-i-1)
    if og%2==0:
        print((og//2)**2)
    else:
        print((og//2 +1 )* (og//2))
    print(ret)
