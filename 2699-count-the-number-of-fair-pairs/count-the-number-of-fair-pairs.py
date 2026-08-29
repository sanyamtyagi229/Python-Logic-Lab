class Solution:
    def countPairs(self, nums, X):
        ans = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= X:
                ans += (right - left)
                left += 1
            else:
                right -= 1
        return ans

    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        return self.countPairs(nums, upper) - self.countPairs(nums, lower - 1)
