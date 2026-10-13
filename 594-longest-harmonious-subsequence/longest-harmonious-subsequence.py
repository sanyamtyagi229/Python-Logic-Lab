from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        count = Counter(nums)
        max_len = 0
        
        for x in count:
            if x + 1 in count:
                max_len = max(max_len, count[x] + count[x + 1])
                
        return max_len