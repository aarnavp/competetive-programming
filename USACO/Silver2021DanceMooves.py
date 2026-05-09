###
# Graph problem with memoization
# Detected cycle via set unions and when I found a key I already created a graph for I just added the number and set of possibilities branching from that key
# This is not a full-solve, it can still be optimized, i should probably try to find a more efficient sol in the future
###
N, K = map(int, input().split())
curr = []
for x in range(1, N+1):
    curr.append(x)

d = {}

for _ in range(K):
    a, b = map(int, input().split())
    a-=1
    b-=1
    if curr[a] not in d:
        d[curr[a]] = [a+1, b+1]
    else:
        d[curr[a]].append(b+1)

    if curr[b] not in d:
        d[curr[b]] =  [b+1, a+1]
    else:
        d[curr[b]].append(a+1)

    temp = curr[a]
    curr[a] = curr[b]
    curr[b] = temp

memo = {}
for key in range(1, N+1):
    if key not in d:
        print(1)
        continue
    if d[key][-1] in memo:
        memo[key] = memo[d[key][-1]] | set(d[key])
        print(len(memo[key]))
        continue
    
        
    res = set()
    visited = []
    res = res | set(d[key])
    rn = key
    while d[rn][-1] not in visited:
        visited.append(d[rn][-1])
        if d[rn][-1] in memo:
            res = res | memo[d[rn][-1]]
            break
        rn = d[rn][-1]
        res = res | set(d[rn])

    memo[key] = res

    print(len(res))
