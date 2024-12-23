from collections import deque

class Solution:
    def minimumOperations(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def min_swaps_to_sort(arr):
            """
            Calcula o número mínimo de trocas para ordenar um array.
            """
            n = len(arr)
            # Cria uma lista de pares (valor, índice original) e ordena pelo valor
            sorted_arr = sorted([(val, idx) for idx, val in enumerate(arr)])
            visited = [False] * n
            swaps = 0

            for i in range(n):
                # Ignora elementos já ordenados ou visitados
                if visited[i] or sorted_arr[i][1] == i:
                    continue

                # Calcula o tamanho do ciclo
                cycle_size = 0
                x = i

                while not visited[x]:
                    visited[x] = True
                    x = sorted_arr[x][1]
                    cycle_size += 1

                # Adiciona ao número de trocas o tamanho do ciclo - 1
                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps

        # Inicializa uma fila para a travessia em largura (BFS)
        queue = deque([root])
        operations = 0

        while queue:
            level_size = len(queue)
            level_values = []

            # Coleta os valores dos nós no nível atual
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                # Adiciona os filhos à fila
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calcula o número mínimo de operações para ordenar os valores do nível
            operations += min_swaps_to_sort(level_values)

        return operations
