# this is an implementation of Kosaraju's 2-pass algorithm to find strong connected components (SCC)
# we use an array of vertex pairs to represent edges

from typing import List
from collections import defaultdict

def find_scc(graph: List[List[int]], n: int) -> List[List[int]]:
    # adjacency list representation of G and G_rev
    adj, adjr = defaultdict(list), defaultdict(list)
    for a, b in graph:
        adj[a].append(b)
        adjr[b].append(a)
    
    seen = set()
    time = [0 for j in range(n)]  # record the order of visit for node i
    t = [0]
    def dfs_rev(g, i):
        seen.add(i)
        for nei in g[i]:
            if nei not in seen:
                dfs_rev(g, nei)        
        time[i] = t[0]
        t[0]+=1

    # traverse G_rev and fill time array 
    for i in range(n-1, -1, -1):
        if i not in seen:
            dfs_rev(adjr, i)   

    # reverse map index to value
    order = [0 for j in range(n)]
    for i in range(n):
        order[time[i]] = i  

    seen = set()
    def dfs(g, i, temp):
        seen.add(i)
        for nei in g[i]:
            if nei not in seen:
                dfs(g, nei, temp)
        temp.append(i+1)

    # traverse G based on order in time array
    res = []
    for j in range(n-1, -1, -1):
        node = order[j]
        if node in seen: continue
        temp = []
        dfs(adj, node, temp)
        res.append(temp)
    
    return res

graph = [[7,1],[1,4],[4,7],[9,3],[3,6],[6,9],[9,7],[8,6],[8,2],[2,5],[5,8]]
graph = [[i-1, j-1] for i, j in graph]
n = 9
print(find_scc(graph, n))