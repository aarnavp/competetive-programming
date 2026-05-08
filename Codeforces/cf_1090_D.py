import math
def sieve(x):
    a = [True]*(x+2)
    
    for i in range(2, x+2):
        if not a[i]:
            continue
        for j in range(2*i, x+1, i):
            a[j] = False
    res = []
    for fin in range(x+2):
        if a[fin]:
            res.append(fin)
    return (res, a)
 
primes = sieve(200000)[0]
 
a = []
for x in range(2, 10002):
    a.append(primes[x]*primes[x+1])
    
t = int(input())
for _ in range(t):
    n = int(input())
    
    
##    gcds = []
##    for i in range(n-1):
##        if math.gcd(res[i],res[i+1]) in gcds:
##            print("OH NO F***!!!!")
##            break
##        gcds.append(math.gcd(res[i],res[i+1]))
        
    print(*a[:n])
