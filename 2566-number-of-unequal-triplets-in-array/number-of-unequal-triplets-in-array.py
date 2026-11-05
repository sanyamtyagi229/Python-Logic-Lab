class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i+1):
                for k in range(j+1):
                    if nums[i]!=nums[j] and nums[j]!=nums[k] and nums[k]!=nums[i]:
                        c=c+1
        return c
        