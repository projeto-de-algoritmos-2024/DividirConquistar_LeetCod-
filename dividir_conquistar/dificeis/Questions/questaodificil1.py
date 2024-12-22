class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Garantir que nums1 seja o menor array para eficiência
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (m + n + 1) // 2 - partition_x

            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]

            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Encontrou a partição correta
                if (m + n) % 2 == 0:
                    # Número par de elementos
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    # Número ímpar de elementos
                    return float(max(max_left_x, max_left_y))
            elif max_left_x > min_right_y:
                # Precisa mover partition_x para a esquerda
                high = partition_x - 1
            else:
                # Precisa mover partition_x para a direita
                low = partition_x + 1

        # Este ponto nunca deve ser alcançado se os arrays forem classificados
        raise ValueError("Os arrays não são classificados ou há um problema.")
