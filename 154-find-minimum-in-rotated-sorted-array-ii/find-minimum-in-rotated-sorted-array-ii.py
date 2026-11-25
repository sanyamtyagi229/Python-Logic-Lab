class Solution:
    def findMin(self, nums: list[int]) -> int:
        s=nums[0]
        for i in range(len(nums)):
            v=nums[i]
            if v<s:
                s=v
        return s