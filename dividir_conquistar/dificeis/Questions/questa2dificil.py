import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Verifica se a lista de listas está vazia ou nula
        if not lists or len(lists) == 0:
            return None

        # Cria um heap mínimo para armazenar os nós
        min_heap = []

        # Adiciona o cabeçalho de cada lista ligada ao heap
        for i, head in enumerate(lists):
            if head:
                # Adiciona ao heap o valor do nó, o índice da lista e o próprio nó
                heapq.heappush(min_heap, (head.val, i, head))

        # Cria um nó fictício para simplificar o processo de mesclagem
        dummy = ListNode(0)
        current = dummy

        # Extrai o menor nó do heap e adiciona à lista mesclada
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            # Conecta o nó extraído à lista mesclada
            current.next = node
            current = current.next

            # Se o nó extraído tiver um próximo nó, adiciona-o ao heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        # Retorna o próximo do nó fictício, que é o início da lista mesclada
        return dummy.next
