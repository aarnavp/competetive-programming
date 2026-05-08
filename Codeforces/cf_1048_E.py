#simple win condition checking if the player who goes first has a non prime number with multiple unique factors

t = int(input())
def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_p[p]:
            for i in range(p * p, n + 1, p):
                is_p[i] = False
    
    
    prime_numbers = [p for p, is_prime in enumerate(is_p) if is_prime]
    return (prime_numbers, is_p)
plug = sieve_of_eratosthenes(10**6)
primes = plug[0]
isprime = plug[1]
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    printed = False
    if sorted(a) == a:
        printed = True
        print('Bob')
    else:
        last = 0
        res = 1
        for x in range(n):
            i = 0
            temp = a[x]
            past = res
            res = 1
            if printed:
                break
 
            if isprime[temp] == True:
                res = temp
            else:
                while primes[i]<=temp**(0.5) and temp!=1:
                    
                    if temp%primes[i] == 0:
                        while temp%primes[i] == 0:
                            temp /= primes[i]
 
                        if temp == 1 and primes[i]>=res:
                            res = primes[i]
 
                        else:
                            
                            res = -1
                            break
                    else:
                        i+=1
            #print(past, res)
            if res>=past and res!=-1 and past!=-1:
                
                pass
            else:
                print('Alice')
                printed = True
                break
 
    if not printed:
        print('Bob')
                        
     
