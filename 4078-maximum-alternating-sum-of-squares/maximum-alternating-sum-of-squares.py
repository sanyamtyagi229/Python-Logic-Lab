class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squared = []
        for x in nums:
            squared.append(x * x)
        squared.sort()
        
        n = len(nums)
        mid = n // 2
        smaller_sum = 0
        for i in range(mid):
            smaller_sum += squared[i]
        larger_sum = 0
        for i in range(mid, n):
            larger_sum += squared[i]
        return larger_sum - smaller_sum