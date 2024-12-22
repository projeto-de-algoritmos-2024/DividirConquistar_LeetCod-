from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        # Estado inicial: (nó atual, máscara de visitação, custo acumulado)
        queue = deque((i, 1 << i, 0) for i in range(n))  # Um estado por nó inicial
        visited = set((i, 1 << i) for i in range(n))  # (nó atual, máscara)

        # BFS para explorar todos os estados
        while queue:
            node, mask, cost = queue.popleft()

            # Se todos os nós foram visitados
            if mask == (1 << n) - 1:
                return cost

            # Explorar os vizinhos
            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)  # Atualiza a máscara
                if (neighbor, next_mask) not in visited:
                    visited.add((neighbor, next_mask))
                    queue.append((neighbor, next_mask, cost + 1))

        return -1  # Nunca alcançável (não esperado para um grafo conectado)
