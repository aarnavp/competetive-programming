t = int(input())
for _ in range(t):
    a, b, x = map(int, input().split())
    diff = abs(a - b)
    res = diff
    counter = 0
    while a != b:
        counter += 1
        if a > b:
            a //= x
        else:
            b //= x

        curr = abs(a - b) + counter
        res = min(res, curr)

    print(res)
    
        
