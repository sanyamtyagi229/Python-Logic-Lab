class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        for x in nums:
            if x<k:
                count+=1
        return count