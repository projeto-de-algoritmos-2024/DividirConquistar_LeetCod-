import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        # Cria o grafo como um dicionário de adjacências
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Usar um heap (fila de prioridade) para o algoritmo de Dijkstra
        min_heap = [(0, k)]  # (tempo acumulado, nó atual)
        min_time = {}  # Armazena o menor tempo para cada nó

        while min_heap:
            time, node = heapq.heappop(min_heap)

            # Se já visitamos o nó com um tempo menor ou igual, ignoramos
            if node in min_time:
                continue

            # Atualiza o tempo mínimo para o nó
            min_time[node] = time

            # Adiciona os vizinhos do nó atual ao heap
            for neighbor, travel_time in graph[node]:
                if neighbor not in min_time:
                    heapq.heappush(min_heap, (time + travel_time, neighbor))

        # Verifica se todos os nós foram alcançados
        if len(min_time) == n:
            return max(min_time.values())  # O maior tempo entre os nós alcançados
        return -1  # Nem todos os nós foram alcançados
