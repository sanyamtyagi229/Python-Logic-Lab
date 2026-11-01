class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        op = 0
        
        while left < right:
            op += nums[right] - nums[left]
            left += 1
            right -= 1
            
        return op