###
# Utilizes BFS via queue
# collections.deque for deque structure (faster than og list)
###
from collections import deque
'''
import sys
sys.stdin = open("fenceplan.in", "r")
sys.stdout = open("fenceplan.out", "w")

#uncomment for submission on usaco

'''

N, M = map(int, input().split())
graph = {}
coords = {}
for i in range(1, N+1):
    x, y = map(int, input().split())
    coords[i] = (x, y)

for _ in range(M):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

visited = [False]*(N+1)
mins = 4*(10**8 + 1)
for cow in graph.keys():
    
    if visited[cow]:
        continue
    else:
        #print(cow)
        visited[cow] = True
        
    Q = deque(graph[cow])
    topx = -1
    topy = -1
    botx = 10**8 + 1
    boty = 10**8 + 1
    if coords[cow][0]>topx:
        topx = coords[cow][0]
    if coords[cow][1]>topy:
        topy = coords[cow][1]
    if coords[cow][0]<botx:
        botx = coords[cow][0]
    if coords[cow][1]<boty:
        boty = coords[cow][1]
        
    while len(Q)>0:
        
        if coords[Q[0]][0]>topx:
            topx = coords[Q[0]][0]
        if coords[Q[0]][1]>topy:
            topy = coords[Q[0]][1]
        if coords[Q[0]][0]<botx:
            botx = coords[Q[0]][0]
        if coords[Q[0]][1]<boty:
            boty = coords[Q[0]][1]

          
        visited[Q[0]] = True
        for x in graph[Q[0]]:
            if visited[x]:
                continue
            else:
                Q.append(x)
                
        Q.popleft()

    if 2*(topx - botx)+2*(topy - boty)<mins and topy - boty!=0 and topx - botx!=0:
        mins = 2*(topx - botx)+2*(topy - boty)
        #print((botx, boty), (topx, topy))
        #print(visited)

print(mins)
