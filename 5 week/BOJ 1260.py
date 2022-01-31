import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[False] * 1001 for _ in range(1001)]

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1][n2] = True

def dfs(graph, V):
    visited = []
    dfs_dq = deque()
    dfs_dq.append(V)
    
    while dfs_dq:
        check = dfs_dq.popleft()
        visited.append(check)
        
        for i in range(1001):
            if graph[check][i]:
                if i not in visited:
                    visited.append(i)
                    dfs_dq.append(i)
                    break
                
    print(visited)
    
dfs(graph, V)