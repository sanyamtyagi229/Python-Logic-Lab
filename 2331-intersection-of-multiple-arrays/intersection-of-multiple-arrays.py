class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        from collections import Counter
        
        counts = Counter()
        for arr in nums:
            counts.update(arr)
            
        n = len(nums)
        result = [num for num, freq in counts.items() if freq == n]

        return sorted(result)