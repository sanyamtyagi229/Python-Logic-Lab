class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n <= 3:
            return 0

        a = nums[n - 3] - nums[0]
        b = nums[n - 1] - nums[2]
        c = nums[n - 2] - nums[1]

        return min(a,b,c)