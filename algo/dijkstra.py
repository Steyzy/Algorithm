# this is the implementation for Dijkstra's shortest-path algorithm

from heap_for_dijkstra import *
from typing import List
from collections import defaultdict, deque

# input graph is in format [u, v, distance]
def dijkstra(graph: List[int], src, dest) -> int:
    # build adjacency list
    adj = defaultdict(list)
    for u, v, d in graph:
        adj[u].append([v, d])
        adj[v].append([u, d])

    # traverse the graph
    seen = set()
    heap, index_map = [], dict()
    score, path = defaultdict(lambda: 100), defaultdict(list)
    score[src] = 0
    while len(seen)<len(adj)-1:
        # pick a vertex by popping from heap
        node = pop(heap, index_map).node if len(seen)>0 else src
        # print("======= "+str(node))
        # mark vertex as visited
        seen.add(node)
        # update scores
        for v, d in adj[node]:
            if v in seen: continue
            # print(v, d)
            if score[node]+d<score[v]:
                score[v] = score[node]+d
                # print(list(score.items()))
                # update or insert vertex v
                if v in index_map:
                    decrease_key(heap, index_map, v, score[v])
                else:
                    insert(heap, index_map, Element(score[v], v))
            # print(list(score.items()))
            # print([vertex.score for vertex in heap])
    
    return score[dest]

graph = [[1,2,1],[1,3,4],[2,3,2],[2,4,6],[3,4,3]]
print(dijkstra(graph, 1, 4))