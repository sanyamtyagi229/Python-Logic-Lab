class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        k = 1
        for x in nums:
            if x == k:
                k += 1
            elif x > k:
                return k
        return k