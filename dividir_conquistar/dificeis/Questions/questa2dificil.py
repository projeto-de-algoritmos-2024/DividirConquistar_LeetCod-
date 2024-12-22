from collections import defaultdict
from heapq import heappop, heappush
import sys
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)
        
        # Construindo o grafo
        for u, v, w in edges:
            graph[u].append((v, w + 1))  # +1 porque cada aresta é dividida em w+1 nós
            graph[v].append((u, w + 1))
        
        # Inicializando distâncias com infinito
        dist = [sys.maxsize] * n
        dist[0] = 0
        
        # Fila de prioridade para o Dijkstra
        pq = [(0, 0)]  # (distância atual, nó atual)
        
        while pq:
            d, u = heappop(pq)
            if d > dist[u]:
                continue
            for v, nd in graph[u]:
                if d + nd < dist[v]:
                    dist[v] = d + nd
                    heappush(pq, (d + nd, v))
        
        # Contando os nós alcançáveis
        ans = sum(1 for d in dist if d <= maxMoves)
        
        # Contando os nós intermediários em cada aresta
        for u, v, w in edges:
            cnt1 = max(maxMoves - dist[u], 0)
            cnt2 = max(maxMoves - dist[v], 0)
            ans += min(cnt1 + cnt2, w)
        
        return ans