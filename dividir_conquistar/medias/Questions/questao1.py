class Solution(object):
    def sortArray(self, nums):
        """
        Ordena o array em ordem crescente usando QuickSort com mediana das medianas.
        :type nums: List[int]
        :rtype: List[int]
        """
        def find_median_of_medians(arr):
            """
            Encontra a mediana usando a técnica de mediana das medianas.
            Divide o array em grupos de 5 e encontra a mediana dos valores medianos.
            """
            if len(arr) <= 5:
                return sorted(arr)[len(arr) // 2]  # Ordena diretamente quando o grupo é pequeno
            
            # Divide o array em grupos de 5
            groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
            # Calcula as medianas de cada grupo
            medians = [sorted(group)[len(group) // 2] for group in groups]
            # Retorna a mediana das medianas
            return find_median_of_medians(medians)
        
        def quicksort(arr):
            """
            Implementa o QuickSort usando mediana das medianas para escolher o pivô.
            """
            if len(arr) <= 1:
                return arr
            
            # Escolhe o pivô com a mediana das medianas
            pivot = find_median_of_medians(arr)
            
            # Particiona o array em relação ao pivô
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            
            # Ordena as partes e junta
            return quicksort(left) + middle + quicksort(right)
        
        # Chama o QuickSort no array fornecido
        return quicksort(nums)