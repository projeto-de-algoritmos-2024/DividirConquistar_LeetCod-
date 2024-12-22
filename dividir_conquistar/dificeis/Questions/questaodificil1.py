class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def select_kth(nums, k):
            # Implementa o algoritmo "Mediana das Medianas"
            if len(nums) <= 5:
                return sorted(nums)[k]

            # Divide o array em grupos de 5
            groups = [nums[i:i+5] for i in range(0, len(nums), 5)]
            medians = [sorted(group)[len(group) // 2] for group in groups]
            
            # Recursivamente encontre a mediana das medianas
            pivot = select_kth(medians, len(medians) // 2)

            # Particione o array em relação ao pivô
            lows = [x for x in nums if x < pivot]
            highs = [x for x in nums if x > pivot]
            pivots = [x for x in nums if x == pivot]

            if k < len(lows):
                return select_kth(lows, k)
            elif k < len(lows) + len(pivots):
                return pivot
            else:
                return select_kth(highs, k - len(lows) - len(pivots))

        def find_median(nums):
            n = len(nums)
            if n % 2 == 0:
                return (select_kth(nums, n // 2 - 1) + select_kth(nums, n // 2)) / 2.0
            else:
                return select_kth(nums, n // 2)

        # Combina os dois arrays
        merged = nums1 + nums2
        return find_median(merged)
