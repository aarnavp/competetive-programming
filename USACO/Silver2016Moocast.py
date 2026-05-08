###
# simple bfs using a visited set
###
from collections import deque
'''
import sys
sys.stdin = open("moocast.in", "r")
sys.stdout = open("moocast.out", "w")
# uncomment for usaco submission
'''
N = int(input())
cows = []
for _ in range(N):
    x, y, p = map(int, input().split())
    cows.append((x, y, p))

graph = {}
for x in range(N):
    graph[x] = []
    for y in range(N):
        if x!=y:
            if (abs(cows[x][0] - cows[y][0])**2 + abs(cows[x][1] - cows[y][1])**2)**0.5 <= cows[x][2]:
                graph[x].append(y)


maxs = 1
for i in graph:
    visited = set()
    q = deque()
    
    visited.add(i)
    q.append(i)

    #print(q)

    while len(q)!=0:
        for x in graph[q[0]]:
            if x not in visited:
                q.append(x)
                visited.add(x)

        q.popleft()

    
        
    maxs = max(maxs, len(visited))

print(maxs)
            
            
    
