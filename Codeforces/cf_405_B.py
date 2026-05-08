from collections import deque
n, m = map(int, input().split())
graph = {}
for _ in range(m):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
 
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]
 
freq = [0]*(n+1)
res = "YES"
for k in graph.keys():
    if freq[k] == 0:
        edges = 0
        nodes = 0
        Q = deque([k])
        while len(Q)>0:
            u = Q.popleft()
            if freq[u] == 0:
                nodes += 1
                for x in range(len(graph[u])):
                    edges+=1
                    if freq[graph[u][x]] == 0:
                        Q.append(graph[u][x])
 
            freq[u] = 1
                    
            #Q.pop(0)
 
        edges = edges//2
        if nodes*(nodes-1)//2 != edges:
            res = "NO"
            break
 
print(res)
