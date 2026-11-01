class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        op = 0
        while left < right:
            op += nums[right] - nums[left]
            right -= 1
        return op