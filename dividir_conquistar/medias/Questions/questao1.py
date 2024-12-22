import heapq
import collections
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Criação do grafo com lista de adjacência
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))
        
        # Probabilidades máximas iniciais (distâncias)
        max_prob = [0.0] * n
        max_prob[start] = 1.0  # Probabilidade inicial para o nó inicial
        
        # Fila de prioridade (max-heap usando probabilidades negativas)
        pq = [(-1.0, start)]  # (-probabilidade, nó)

        while pq:
            prob, cur = heapq.heappop(pq)
            prob = -prob  # Reverter para positivo
            
            # Se chegarmos ao destino, retornamos a probabilidade máxima
            if cur == end:
                return prob
            
            # Expandir vizinhos do nó atual
            for nei, edgeProb in adj[cur]:
                new_prob = prob * edgeProb
                if new_prob > max_prob[nei]:  # Apenas atualizar se for uma probabilidade maior
                    max_prob[nei] = new_prob
                    heapq.heappush(pq, (-new_prob, nei))  # Adicionar o vizinho com a nova probabilidade

        return 0